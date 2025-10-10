class Account:
    def __init__(self, balance):
        self.__balance = balance

    def add(self, money):
        self.__balance += money
    
    def minus(self, money):
        if self.__balance < money:
            print("Недостатньо коштів!")
        else:
            self.__balance -= money

    def __str__(self):
        return(str(self.__balance))
    
    def __call__(self):
        return self.__balance

acc1 = Account(1000)
print(acc1)
acc1.add(1000)
acc1.__balance = 50000
print(acc1)
acc1.minus(1500)
print(acc1)
print(acc1())