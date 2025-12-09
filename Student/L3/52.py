seats = ['_', '_', '_', '_', '_']  

def show_seats():
    print("\n" + " ".join(seats))

def seat_num():
    seat_number = input("Введіть номер місця (1-5) або 0 для виходу: ")

    if seat_number == "0":
        print("Вихід...")
        exit()

    if not seat_number.isdigit() or not (1 <= int(seat_number) <= 5):
        print("Помилка: введіть число 1-5 або 0.")
        seat_num()
        return
    
    index = int(seat_number) - 1

    action = input("Введіть дію: 1 — забронювати, 2 — скасувати бронь, 3-купити VIP")

    if action == "1":
        if seats[index] == '_':
            seats[index] = 'X'
        else:
            print("місце вже зайнято")

    elif action == "2":  
        if seats[index] == 'X' or seats[index]=="V":
            seats[index] = '_'
        else:
            print("там і так нічого немає")
    else:
        if seats[index] == "X" or seats[index]=="_":
            seats[index] = "V"
        else:
            print("місцу вже VIP")
    
while True:
    show_seats()
    seat_num()

        

