def add_food():
    food = input("Ввеідть товар: ")
    foods.append(food)

def remove_food():
    food = input("Введіть товар: ")
    if food in foods:
        foods.remove(food)
    else:
        print("Такого товару немає")

def view_foods():
    if not foods:
        print("Список порожній")
    else:
        line = "-" * 35
        print(line)
        print("|{:>2}|{:^30}|".format("№", "Назва товару"))
        print(line)
        for i, food in enumerate(foods):
            print("|{:>2}|{:<30}|".format(i + 1, food))
        print(line)

foods = ["хліб", "масло", "молоко"]

while True:
    print("1. Додати")
    print("2. Видалити")
    print("3. Переглянути")
    print("4. Вихід")

    cmd = int(input("Введіть команду: "))

    if cmd == 1:
        add_food()
    elif cmd == 2:
        remove_food()
    elif cmd == 3:
        view_foods()
    elif cmd == 4:
        break
    else:
        print("Невідома команда")