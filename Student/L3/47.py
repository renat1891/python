class Tasks:
    def __init__(self):
        self.to_do = []

    def print_task(self):
        print("\nПоточний список справ:")

        if len(self.to_do) == 0:
            print("Список справ порожній")
        else:
            for i, task in enumerate(self.to_do, start=1):
                print(f"{i}. {task}")

    def add_new_task(self):
        user_input = input("Введіть нову справу (або 0 для виходу): ")


        if user_input == "0":
            print("Вихід з програми")
            exit()

        elif user_input == "-1":
            if len(self.to_do) == 0:
                print("Список справ порожній")
            else:
                self.to_do.pop()
        elif user_input == "del":
            num_del = int(input("введіть номер який хочете видалити: "))
            self.to_do.pop(num_del-1)
        else:
            if len(self.to_do) == 5:
                print("зробіть попередні справи")
            else:
                self.to_do.append(user_input)


task = Tasks()

while True:
    task.print_task()
    task.add_new_task()

    