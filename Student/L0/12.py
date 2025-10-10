
def add_coach():
    name = input("Введіть ім'я дресирувальника: ")
    if name in coaches:
        print(" Такий дресирувальник вже існує!")
        return

    num_dragons = int(input("Введіть кількість драконів: "))
    avg_power = int(input("Введіть середній рівень сили (1-100): "))

    coaches[name] = {
        "num_dragons": num_dragons,
        "avg_power": avg_power
    }
    print(f" Дресирувальника {name} додано!")


def calc_rating(num_dragons, avg_power):
    
    return num_dragons * avg_power


def get_title(rating):
    if rating < 300:
        return 
    elif rating <= 1000:
        return 
    else:
        return


def show_coaches():
    if not coaches:
        print("Список порожній")
        return

    for name in coaches:
        rating = calc_rating(coaches[name]["num_dragons"], coaches[name]["avg_power"])
        title = get_title(rating)
        print(f"\n{name}")
        print(f"   Драконів: {coaches[name]['num_dragons']}")
        print(f"   Середня сила: {coaches[name]['avg_power']}")
        print(f"   Рейтинг: {rating}")
        print(f"   Титул: {title}")


def delete_coach():
    name = input("Введіть ім'я для видалення: ")
    if name in coaches:
        del coaches[name]
        print(f" Дресирувальника {name} видалено")
    else:
        print(" Такого імені немає")


def find_coach():
    name = input("Введіть ім'я для пошуку: ")
    if name in coaches:
        rating = calc_rating(coaches[name]["num_dragons"], coaches[name]["avg_power"])
        title = get_title(rating)
        print(f"\n{name}")
        print(f"   Драконів: {coaches[name]['num_dragons']}")
        print(f"   Середня сила: {coaches[name]['avg_power']}")
        print(f"   Рейтинг: {rating}")
        print(f"   Титул: {title}")
    else:
        print(" Дресирувальника не знайдено")



coaches = {
    "Аліса": {"num_dragons": 5, "avg_power": 40},
    "Боб": {"num_dragons": 12, "avg_power": 60},
    "Чарлі": {"num_dragons": 20, "avg_power": 55}
}



while True:
    print("1. Додати дресирувальника")
    print("2. Показати список")
    print("3. Видалити дресирувальника")
    print("4. Знайти дресирувальника")
    print("5. Вихід")

    try:
        cmd = int(input("Введіть команду: "))
    except ValueError:
        print(" Помилка! Введіть число.")
        continue

    if cmd == 1:
        add_coach()
    elif cmd == 2:
        show_coaches()
    elif cmd == 3:
        delete_coach()
    elif cmd == 4:
        find_coach()
    elif cmd == 5:
        print(" Програму завершено")
        break
    else:
        print(" Невідома команда")