def add_researcher():
    name = input("Ввеідть ім'я: ")
    num_artifacts = int(input("Введіть кількість артефактів: "))
    avg_artifact_rarity = int(input("Введіть середню рідкість артефакту: "))
    researchers[name]={
        "artifacts": num_artifacts,
        "artifact_rarity": avg_artifact_rarity,
    }
    
    print(f"Дослідника {name} додано")

def show_researchers():
    print(researchers)

def kategory_researchers():
    
    for name, val in researchers.items():
        rating = val['num_artifacts'] * val['avg_artifact_rarity']
        
        if rating < 50:
            category = "Новачок"
        elif 50 <= rating <= 200:
            category = "Майстер"
        else:
            category = "Архіваріус"
        
        print(f"\nДослідник: {name}")
        print(f"Кількість артефактів: {val['num_artifacts']}")
        print(f"Середня рідкість: {val['avg_artifact_rarity']}")
        print(f"Рейтинг: {rating}")
        print(f"Категорія: {category}")

def delete_researcher():
    name = input("Введіть ім'я: ")
    if name in researchers:
        del researchers[name]
        print(f"Дослідника {name} видалено")
    else:
        print(f"Дослідника з ім'ям {name} не знайдено")

def find_researcher():
    name = input("Введіть ім'я: ")
    if name in researchers:
        print(researchers[name])
    else:
        print(f'Дослідника {name} не знайдено')
    
researchers = {
    "Alice": {
        "num_artifacts": 90,
        "avg_artifact_rarity": 8,
    },
    "Bob": {
        "num_artifacts": 78,
        "avg_artifact_rarity": 2,
    },
    "Charlie": {
        "num_artifacts": 95,
        "avg_artifact_rarity": 9,
        
    }
}


while True:
    print("1. Додати")
    print("2. Показати")
    print("3. Категорія")
    print("4. Видалити")
    print("5. Знайти")
    print("6. вихід")

    cmd = int(input("Введіть команду: "))

    if cmd == 1:
        add_researcher()
    elif cmd == 2:
        show_researchers()
    elif cmd == 3:
        kategory_researchers()
    elif cmd == 4:
        delete_researcher()
    elif cmd == 5:
        find_researcher()
    elif cmd == 6:
        print("Програму закрито")
        break 
    else:
        print("Невідома команда")