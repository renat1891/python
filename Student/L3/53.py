fruits = []  

while True:
    if len(fruits) == 0:
        print("Склад порожній")
    else:
        print("Склад:")
        for i, fruit in enumerate(fruits, start=1):
            print(f"{i}. {fruit}")

    command = input("Введіть назву фрукта для додавання, 'del' щоб видалити, або 0 для виходу: ")

    if command == "0":
        print("Вихід...")
        break

    if command == "del":
        if len(fruits) == 0:
            print("Немає що видаляти!")
            continue

        num = input("Введіть номер для видалення: ")

        if not num.isdigit():
            print("Помилка: введіть число!")
            continue

        num = int(num)

        if 1 <= num <= len(fruits):
            removed = fruits.pop(num - 1)
            print(f"Видалено: {removed}")
        else:
            print("Помилка: такого номера не існує")
        continue

    fruits.append(command)
    print(f"Додано: {command}")
