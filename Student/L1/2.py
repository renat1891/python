# Реалізуйте клас "Rectangle", який має атрибути "width" та "height", які відповідають за ширину та висоту прямокутника відповідно. Клас повинен також мати методи "area()" та "perimetr()", який повертає площу прямокутника та периметр відповідно.
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         print(self.width * self.height)
    
#     def perimetr(self):
#         print(2 * (self.width + self.height))

# rect1 = Rectangle(2, 8)
# rect1.area()
# rect1.perimetr()



# Реалізувати клас "Account", який має поле "balance" , що відповідають за баланс рахунку. Клас повинен мати метод "add()", який додає вказану суму до балансу рахунку, та метод "minus()", який знімає з рахунку вказану суму, якщо на рахунку достатньо коштів.



# class Account:
#     def __init__(self, balance):
#         self.balance = balance

#     def add(self, money):
#         self.balance += money
    
#     def minus(self, money):
#         if self.balance < money:
#             print("Недостатньо коштів!")
#         else:
#             self.balance -= money
    
# acc1 = Account(1000)
# print(acc1.balance)
# acc1.add(1000)
# print(acc1.balance)
# acc1.minus(1500)
# print(acc1.balance)

