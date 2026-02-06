from db_foods import DB


new_db = DB()

def add_food():
    name = input("Назва їжі: ")
    weight = int(input("Вага їжі: "))
    price = int(input("Ціна їжі: "))
    new_db.add_food(name, weight, price)

def get_all_foods():
    foods = new_db.get_all_foods()
    # table format
    print("-"*50)
    print(f"{'ID':<5} {'Назва':<20} {'Вага':<10} {'Ціна':<10}")
    for food in foods:
        print(f"{food.id:<5} {food.name:<20} {food.weight:<10} {food.price:<10}")
    print("-"*50)


def delete_food(food_id):
    food_id = int(input("ID їжі для видалення: "))
    if new_db.get_food_by_id(food_id):
        new_db.delete_food(food_id)
    else:
        print("Їжа з таким ID не знайдена.")

def update_food():
    food_id = int(input("ID їжі для редагування: "))
    name = input("Нова назва їжі: ")
    weight = int(input("Нова вага їжі: "))
    price = int(input("Нова ціна їжі: "))
    new_db.update_food(food_id, name, weight, price)

while True:
    print("1. Додати їжу")
    print("2. Показати всю їжу")
    print("3. Видалити їжу")
    print("4. Редагувати їжу")
    print("5. Вихід")
    command = input("Виберіть дію: ")
    if command == "1":
        add_food()
    elif command == "2":
        get_all_foods()
    elif command == "3":
        delete_food()
    elif command == "4":
        update_food()
    elif command == "5":
        break
    else:
        print("Невірна команда, спробуйте ще раз.")
