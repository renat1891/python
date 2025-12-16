def show_bulbs(bulbs):
    print("Стан лампочок:", ' '.join(bulbs))


def toggle_bulb(number):
    index = number - 1
    if bulbs[index] == '0':
        bulbs[index] = '1'
    else:
        bulbs[index] = '0'


bulbs = ['1', '0', '1', '0']

while True:
    show_bulbs()
    choice = int(input("Виберіть лампочку (1-4) або 0 для виходу: "))

    if choice == 0:
        print("Вихід з програми.")
        break
    elif 1 <= choice <= 4:
        toggle_bulb(bulbs, choice)
    else:
        print("Невірний номер")
