# pip install telethon
from telethon.sync import TelegramClient
from telethon.tl.types import (
    UserStatusOnline, 
    UserStatusRecently, 
    UserStatusLastWeek,
    UserStatusLastMonth
)

# Твої облікові дані з my.telegram.org
api_id = '28263289'
api_hash = 'e582e8f17205d71b93bd6083adeb2ded'
phone = '380688258148'
group_username = 'dim_lviv' # наприклад, 'my_group' (без @) або ID групи

# Створення клієнта
client = TelegramClient('session_name', api_id, api_hash)

async def main():
    await client.start(phone=phone)
    print("Успішно підключено до Telegram!")

    print(f"Збираємо дані з групи {group_username}...")
    
    # get_participants автоматично обробляє пагінацію для великих груп
    participants = await client.get_participants(group_username)
    
    active_users = []

    for user in participants:
        # 1. Відсіюємо ботів та видалені акаунти
        if user.bot or user.deleted:
            continue
            
        # 2. Відсіюємо тих, у кого немає юзернейму (якщо потрібні саме @ніки)
        if not user.username:
            continue

        # 3. Фільтрація за активністю
        # Telegram не дає точний час для тих, хто його приховав, але дає приблизний статус
        is_active = False
        if isinstance(user.status, (UserStatusOnline, UserStatusRecently, UserStatusLastWeek)):
            is_active = True
            
        # Якщо потрібно включити тих, хто був у мережі до місяця тому, розкоментуй рядок нижче:
        # if isinstance(user.status, UserStatusLastMonth): is_active = True

        if is_active:
            active_users.append(user.username)
            # Можна відразу записувати у файл, тут просто виводимо для прикладу
            print(f"Додано: @{user.username}")

    print(f"\nГотово! Зібрано {len(active_users)} активних користувачів.")

    # Збереження у TXT файл
    with open(f"{group_username}.txt", "w", encoding="utf-8") as f:
        for username in active_users:
            f.write(f"@{username}\n")

with client:
    client.loop.run_until_complete(main())