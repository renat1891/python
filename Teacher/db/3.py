from db import DB

new_db = DB()

while True:
    print("1. Додати")
    print("2. Показати")
    print("3. Видалити всіх")
    print("4. Видалити особу")
    print("5. Вийти")
    cmd = int(input("Введіть команду: "))
    if cmd == 1:
        name = input("Введіть імя")
        age = int(input("Введіть вік"))
        new_db.add_person(name, age)
    elif cmd == 2:
        new_db.show_people()
    elif cmd == 3:
        new_db.delete_people()
    elif cmd == 4:
        name = input("Введіть імя")
        new_db.delete_person(name)
    elif cmd == 5:
        new_db.exit()    
    else:
        print("Невідома команда")


# Bank bot
# при реєстрації банк дає 100 грн на рахунок
# користувач може переказати гроші іншому користувачу по id/nikнейму
# користувач може подивитись свій баланс
# користувач може покласти гроші на депозит під 10% на день заокругляючи суму в більшу сторону до копійок(шаги)
# користувач може зняти гроші з депозиту (він отримує суму + відсотки)
# користувач може подивится на свій депозит