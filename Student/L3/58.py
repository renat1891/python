import json

def save_to_json(data):
    with open("1.json", 'w') as file:
        json.dump(data, file, indent=4)

def load_from_json():
    try:
        with open("1.json", 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def show_passwords(passwords):
    if not passwords:
        print("Паролів немає")
    else:
        for i, pwd in enumerate(passwords, start=1):
            print(i, pwd)


def add_password(passwords):
    pwd = input("Введіть новий пароль: ")
    passwords.append(pwd)
    save_to_json(passwords)


def delete_password(passwords):
    if not passwords:
        print("Список порожній")
        return
    

    num = int(input("Введіть номер пароля для видалення: "))
    if 1 <= num <= len(passwords):
        passwords.pop(num - 1)
        save_to_json(passwords)
    else:
        print("Невірний номер")


passwords = load_from_json()

while True:
    print("\nКількість паролів:", len(passwords))
    command = input("add — додати, del — видалити, show — показати, 0 — вихід: ")

    if command == '0':
        print("Вихід з програми.")
        break
    elif command == 'add':
        add_password(passwords)
    elif command == 'del':
        delete_password(passwords)
    elif command == 'show':
        show_passwords(passwords)
    else:
        print("Невідома команда")
