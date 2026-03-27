"""
Telegram Group Members Scraper
==============================
Скрипт для отримання списку учасників Telegram-групи з фільтрацією.
 
Встановлення:
    pip install telethon
 
Налаштування:
    1. Зайди на https://my.telegram.org/apps
    2. Створи додаток і отримай API_ID та API_HASH
    3. Впиши їх нижче або передай через аргументи командного рядка
 
Використання:
    python telegram_members_scraper.py --group "назва_або_посилання_групи"
 
    Приклади:
    python telegram_members_scraper.py --group "my_chat" --output members.csv
    python telegram_members_scraper.py --group "my_chat" --no-bots --no-deleted --min-days 30
    python telegram_members_scraper.py --group "my_chat" --recently-online --has-username
"""
 
import argparse
import asyncio
import csv
import json
import sys
from datetime import datetime, timezone, timedelta
 
from telethon import TelegramClient
from telethon.tl.types import (
    UserStatusOnline,
    UserStatusOffline,
    UserStatusRecently,
    UserStatusLastWeek,
    UserStatusLastMonth,
    UserStatusEmpty,
    ChannelParticipantsAdmins,
    ChannelParticipantsRecent,
    ChannelParticipantsSearch,
)
from telethon.tl.functions.channels import GetFullChannelRequest
 
# ============================================================
# ⚙️ НАЛАШТУВАННЯ — впиши свої значення або передай аргументами
# ============================================================
API_ID = 0           # Заміни на свій API ID (число)
API_HASH = ""        # Заміни на свій API HASH (рядок)
PHONE = ""           # Твій номер телефону, наприклад: "+380XXXXXXXXX"
SESSION_NAME = "scraper_session"
 
 
def parse_args():
    parser = argparse.ArgumentParser(
        description="Telegram Group Members Scraper — парсер учасників групи"
    )
 
    # Основні параметри
    parser.add_argument(
        "--group", "-g",
        required=True,
        help="Username групи (без @), invite-посилання або ID групи"
    )
    parser.add_argument(
        "--output", "-o",
        default="members.csv",
        help="Файл для збереження результатів (csv/json). За замовчуванням: members.csv"
    )
 
    # API-дані (можна передати замість хардкоду)
    parser.add_argument("--api-id", type=int, default=None, help="Telegram API ID")
    parser.add_argument("--api-hash", default=None, help="Telegram API Hash")
    parser.add_argument("--phone", default=None, help="Номер телефону для авторизації")
 
    # ──────────── ФІЛЬТРИ ────────────
 
    # Фільтр ботів
    parser.add_argument(
        "--no-bots",
        action="store_true",
        help="Виключити ботів"
    )
 
    # Фільтр видалених акаунтів
    parser.add_argument(
        "--no-deleted",
        action="store_true",
        help="Виключити видалені акаунти"
    )
 
    # Фільтр преміум-користувачів
    parser.add_argument(
        "--premium-only",
        action="store_true",
        help="Тільки преміум-користувачі"
    )
 
    # Фільтр за юзернеймом
    parser.add_argument(
        "--has-username",
        action="store_true",
        help="Тільки користувачі з @username"
    )
 
    # Фільтр за фото
    parser.add_argument(
        "--has-photo",
        action="store_true",
        help="Тільки користувачі з аватаркою"
    )
 
    # Фільтр за онлайн-статусом
    parser.add_argument(
        "--recently-online",
        action="store_true",
        help="Тільки ті, хто був онлайн нещодавно (recently/online/last week)"
    )
 
    # Фільтр за останнім онлайном (в днях)
    parser.add_argument(
        "--max-offline-days",
        type=int,
        default=None,
        help="Максимум днів з останнього онлайну (працює лише для видимих статусів)"
    )
 
    # Фільтр за датою реєстрації в групі
    parser.add_argument(
        "--min-days",
        type=int,
        default=None,
        help="Мінімум днів в групі (відфільтрує новачків)"
    )
 
    # Фільтр за іменем (пошук)
    parser.add_argument(
        "--search",
        default=None,
        help="Пошук за іменем/прізвищем/юзернеймом"
    )
 
    # Тільки адміни
    parser.add_argument(
        "--admins-only",
        action="store_true",
        help="Отримати тільки адміністраторів"
    )
 
    # Ліміт
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Максимальна кількість учасників для отримання"
    )
 
    return parser.parse_args()
 
 
def get_last_online(user):
    """Повертає datetime останнього онлайну або описовий рядок."""
    status = user.status
    if isinstance(status, UserStatusOnline):
        return "online", datetime.now(timezone.utc)
    elif isinstance(status, UserStatusOffline):
        return status.was_online.strftime("%Y-%m-%d %H:%M"), status.was_online
    elif isinstance(status, UserStatusRecently):
        return "recently", datetime.now(timezone.utc) - timedelta(days=1)
    elif isinstance(status, UserStatusLastWeek):
        return "last_week", datetime.now(timezone.utc) - timedelta(days=7)
    elif isinstance(status, UserStatusLastMonth):
        return "last_month", datetime.now(timezone.utc) - timedelta(days=30)
    else:
        return "unknown", None
 
 
def is_recently_online(user):
    """Перевіряє чи був користувач онлайн нещодавно."""
    status = user.status
    return isinstance(status, (UserStatusOnline, UserStatusRecently, UserStatusLastWeek))
 
 
def apply_filters(user, args, joined_date=None):
    """Застосовує всі фільтри до користувача. Повертає True якщо пройшов."""
 
    # Боти
    if args.no_bots and user.bot:
        return False
 
    # Видалені акаунти
    if args.no_deleted and user.deleted:
        return False
 
    # Преміум
    if args.premium_only and not getattr(user, "premium", False):
        return False
 
    # Username
    if args.has_username and not user.username:
        return False
 
    # Фото
    if args.has_photo and not user.photo:
        return False
 
    # Нещодавно онлайн
    if args.recently_online and not is_recently_online(user):
        return False
 
    # Максимум днів офлайн
    if args.max_offline_days is not None:
        _, last_dt = get_last_online(user)
        if last_dt is None:
            return False
        days_offline = (datetime.now(timezone.utc) - last_dt.replace(tzinfo=timezone.utc) 
                        if last_dt.tzinfo is None else 
                        datetime.now(timezone.utc) - last_dt).days
        if days_offline > args.max_offline_days:
            return False
 
    # Мінімум днів в групі
    if args.min_days is not None and joined_date:
        days_in_group = (datetime.now(timezone.utc) - joined_date.replace(tzinfo=timezone.utc)
                         if joined_date.tzinfo is None else
                         datetime.now(timezone.utc) - joined_date).days
        if days_in_group < args.min_days:
            return False
 
    return True
 
 
def format_member(user, joined_date=None):
    """Форматує інфо про користувача в dict."""
    last_online_str, _ = get_last_online(user)
 
    return {
        "user_id": user.id,
        "username": user.username or "",
        "first_name": user.first_name or "",
        "last_name": user.last_name or "",
        "phone": user.phone or "",
        "is_bot": user.bot,
        "is_deleted": user.deleted,
        "is_premium": getattr(user, "premium", False),
        "has_photo": bool(user.photo),
        "last_online": last_online_str,
        "joined_date": joined_date.strftime("%Y-%m-%d %H:%M") if joined_date else "",
    }
 
 
async def main():
    args = parse_args()
 
    # Визначення API-даних
    api_id = args.api_id or API_ID
    api_hash = args.api_hash or API_HASH
    phone = args.phone or PHONE
 
    if not api_id or not api_hash:
        print("❌ Помилка: вкажіть API_ID та API_HASH!")
        print("   Отримати можна тут: https://my.telegram.org/apps")
        print("   Впишіть у скрипт або передайте через --api-id і --api-hash")
        sys.exit(1)
 
    # Підключення
    client = TelegramClient(SESSION_NAME, api_id, api_hash)
    await client.start(phone=phone)
    print("✅ Авторизація успішна!")
 
    # Отримання групи
    try:
        entity = await client.get_entity(args.group)
    except Exception as e:
        print(f"❌ Не вдалося знайти групу '{args.group}': {e}")
        await client.disconnect()
        sys.exit(1)
 
    # Інфо про групу
    try:
        full = await client(GetFullChannelRequest(entity))
        total = full.full_chat.participants_count
        print(f"📊 Група: {entity.title}")
        print(f"📊 Всього учасників: {total}")
    except Exception:
        print(f"📊 Група: {getattr(entity, 'title', args.group)}")
 
    # Отримання учасників
    print("\n⏳ Завантаження учасників...")
    members = []
    count = 0
 
    if args.admins_only:
        # Тільки адміни
        async for user in client.iter_participants(entity, filter=ChannelParticipantsAdmins):
            if args.limit and count >= args.limit:
                break
 
            joined = getattr(user.participant, "date", None) if hasattr(user, "participant") else None
 
            if apply_filters(user, args, joined):
                members.append(format_member(user, joined))
                count += 1
 
            if count % 100 == 0 and count > 0:
                print(f"   ... оброблено {count} учасників")
    else:
        # Всі учасники
        async for user in client.iter_participants(
            entity,
            search=args.search or "",
            limit=args.limit
        ):
            joined = getattr(user.participant, "date", None) if hasattr(user, "participant") else None
 
            if apply_filters(user, args, joined):
                members.append(format_member(user, joined))
                count += 1
 
            if count % 500 == 0 and count > 0:
                print(f"   ... оброблено {count} учасників")
 
    print(f"\n✅ Знайдено {len(members)} учасників після фільтрації")
 
    # Збереження
    output = args.output
    if output.endswith(".json"):
        with open(output, "w", encoding="utf-8") as f:
            json.dump(members, f, ensure_ascii=False, indent=2)
    else:
        if not output.endswith(".csv"):
            output += ".csv"
        with open(output, "w", encoding="utf-8", newline="") as f:
            if members:
                writer = csv.DictWriter(f, fieldnames=members[0].keys())
                writer.writeheader()
                writer.writerows(members)
 
    print(f"💾 Збережено у файл: {output}")
 
    # Статистика
    bots = sum(1 for m in members if m["is_bot"])
    deleted = sum(1 for m in members if m["is_deleted"])
    with_username = sum(1 for m in members if m["username"])
    premium = sum(1 for m in members if m["is_premium"])
    with_photo = sum(1 for m in members if m["has_photo"])
 
    print(f"\n{'='*40}")
    print(f"📈 СТАТИСТИКА")
    print(f"{'='*40}")
    print(f"   Всього після фільтрації: {len(members)}")
    print(f"   З @username:             {with_username}")
    print(f"   З аватаркою:             {with_photo}")
    print(f"   Premium:                 {premium}")
    print(f"   Боти:                    {bots}")
    print(f"   Видалені акаунти:        {deleted}")
 
    await client.disconnect()
 
 
if __name__ == "__main__":
    asyncio.run(main())