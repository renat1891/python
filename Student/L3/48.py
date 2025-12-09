class SeatManager:
    def __init__(self, total_seats=5):
        self.seats = ['_'] * total_seats

    def show_seats(self):
        print("\n" + " ".join(self.seats))

    def book_seat(self, index):
        if self.seats[index] == '_':
            self.seats[index] = 'X'
        else:
            print("Місце вже зайнято.")

    def cancel_booking(self, index):
        if self.seats[index] == 'X':
            self.seats[index] = '_'
        else:
            print("Там і так нічого немає.")

    def count_free(self):
        return self.seats.count('_')

    def count_taken(self):
        return self.seats.count('X')

    def reset_all(self):
        self.seats = ['_'] * len(self.seats)
        print("Всі місця очищено.")

    def process(self):
        print("\nДії:")
        print("1 — забронювати місце")
        print("2 — скасувати бронь")
        print("3 — показати кількість вільних місць")
        print("4 — показати кількість зайнятих місць")
        print("5 — очистити всі місця")
        print("0 — вихід")

        action = input("Виберіть дію: ")

        if action == "0":
            print("Вихід...")
            exit()

        if action == "3":
            print("Вільних місць:", self.count_free())
            return
        elif action == "4":
            print("Зайнятих місць:", self.count_taken())
            return
        elif action == "5":
            self.reset_all()
            return

        if action in ("1", "2"):
            seat_number = input("Введіть номер місця (1-5): ")

            if not seat_number.isdigit() or not (1 <= int(seat_number) <= len(self.seats)):
                print("Помилка: введіть число 1-5.")
                return

            index = int(seat_number) - 1

            if action == "1":
                self.book_seat(index)
            elif action == "2":
                self.cancel_booking(index)

        else:
            print("Невірна дія.")


manager = SeatManager()

while True:
    manager.show_seats()
    manager.process()
