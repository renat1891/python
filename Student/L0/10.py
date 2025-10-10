def add_student():
    name = input("Ввеідть ім'я: ")
    age = int(input("Введіть вік: "))
    grade_math = int(input("Введіть оцінку з математики: "))
    grade_physic = int(input("Введіть оцінку з фізики: "))
    grade_ukr = int(input("Введіть оцінку з укр.мови: "))
    students[name]={
        "math": grade_math,
        "physics": grade_physic,
        "ukr": grade_ukr,
        "age":age 
    }
    print(f"Студента {name} додано")

def show_students():
    print(students)

def avg_grades():
    avg = 0
    for val in students.values():
        avg += (val['math'] + val['ukr'] + val["physic"]) / 3
    avg /= len(students)
    avg = round(avg, 2)
    print(f"Середій бал всіх студентів {avg}")

def delete_student():
    name = input("Ввеідть ім'я: ")
    del students[name]
    print(f"Студента {name} видалено")

def find_student():
    name = input("Ввеідть ім'я: ")
    if name in students:
        print(students[name])
    else:
        print(f'Студента {name} не знайдено')

students = {
    "Alice": {
        "math": 90,
        "ukr": 85,
        "physic": 88,
        "age": 20
    },
    "Bob": {
        "math": 78,
        "ukr": 82,
        "physic": 80,
        "age": 21
    },
    "Charlie": {
        "math": 95,
        "ukr": 90,
        "physic": 92,
        "age": 19
    }
}

while True:
    print("1. Додати")
    print("2. Показати")
    print("3. Середній Бал")
    print("4. Видалити")
    print("5. Знайти")
    print("6. вихід")

    cmd = int(input("Введіть команду: "))

    if cmd == 1:
        add_student()
    elif cmd == 2:
        show_students()
    elif cmd == 3:
        avg_grades()
    elif cmd == 4:
        delete_student()
    elif cmd == 5:
        find_student()
    elif cmd == 6:
        print("Програму закрито")
        break 
    else:
        print("Невідома команда")