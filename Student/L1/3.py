# Створіть клас Circle, який буде мати методи для обчислення площі та периметра кола.


# import math

# class Circle:
#     def __init__(self, r):
#         self.r = r

#     def area(self):
#         print(math.pi * self.r ** 2)

#     def perimetr(self):
#         print(2 * math.pi * self.r)

# rect1 = Circle(2)
# rect1.area()
# rect1.perimetr()






# Створіть клас Player, який представляє гравця у грі. Додайте методи для збільшення рівня та відображення поточного рівня і очок. При додаванні певної кількості балів збільшується його рівень


# class Player:
#     def __init__(self, name):
#        self.name = name
#        self.level = 1
#        self.score = 0

#     def add_score(self, points):
#         self.score += points
#         if self.score >= 100:
#             self.level += 1 
#             self.score -= 100
    
#     def info(self):
#         print(self.name, self.level, self.score)


# p1 = Player('Данило')
# p1.info()
# p1.add_score(120)
# p1.info()




# class Time:
#     def __init__(self, hours, minutes, seconds):
#         self.hours = hours
#         self.minutes = minutes
#         self.seconds = seconds

#     def to_seconds(self):
#         return self.hours * 3600 + self.minutes * 60 + self.seconds

#     def show(self):
#         print(f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}")


# t = Time(2, 30, 15)
# print(t.to_seconds())  
# t.show()
        

# class ShoppingCart:
#     def __init__(self):
#        self.items = {}

#     def add_item(self, name, price):
#         self.items[name] = price

#     def remove_item(self, name):
#         if name in self.items:
#             del self.items[name]

#     def total_price(self):
#         return sum(self.items.values())



# cart = ShoppingCart()
# cart.add_item("Хліб", 20)
# cart.add_item("Молоко", 15)
# cart.remove_item("Хліб")
# print(cart.total_price())











# class PassengerPlane:
#     def __init__(self, model, seats):
#         self.model = model
#         self.seats = seats
#         self.passengers = 0

#     def add_passengers(self, count):
#         if self.passengers + count <= self.seats:
#             self.passengers += count
#             print(f"Додано {count} пасажирів. Загалом на борту: {self.passengers}")
#         else:
#             print("Недостатньо місць на борту!")

#     def remove_passengers(self, count):
#         if self.passengers - count >= 0:
#             self.passengers -= count
#             print(f"Видалено {count} пасажирів. Загалом на борту: {self.passengers}")
#         else:
#             print("На борту стільки пасажирів немає!")

#     def __str__(self):
#         return f"Модель: {self.model}, Місць: {self.seats}, Пасажирів: {self.passengers}"



# plane = PassengerPlane("Boeing 737", 180)
# print(plane)

# plane.add_passengers(50)
# plane.add_passengers(140)   
# plane.remove_passengers(20)
# plane.remove_passengers(100)  

# print(plane)