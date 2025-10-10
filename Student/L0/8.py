# with open("1.txt", "r") as  file:
#     text = file.read()
# text = text.lower()
# with open("2.txt", "w") as file:
#     file.write(text)

# def square(a, b):
#     print(a*b)


# square(3, 5)



    
#  square (45, 156)

# def max_num(a, b):
#     if a > b:
#         print(a)
#     elif a == b:
#         print("рівні")
#     else:
#         print(b)


# max_num(5, 5)



# def multiclipation(a, b):
#     return a*b

# m  = multiclipation(2, 8)
# m2 = multiclipation(3, 8)

# print(m + m2)




# def sum_positive(a):
#     suma = 0
#     for i in a:
#         if i > 0:
#             suma+=i
#     return suma

# print(sum_positive([1, -4, 7, 12]))





# my_products = [
#     ["apple", 10],
#     ["banana", 20],
#     ["orange", 30],
#     ["grape", 40],
#     ["kiwi", 50]
# ]

# line = "-" * 34
# print(line)
# print("|{:10}|{:10}|{:10}|".format("#", "ім'я", "ціна"))
# print(line)

# for i, product in enumerate(my_products, start= 1):
#     print("|{:10}|{:10}|{:10}|".format(i, product[0], product[1]))


# print(line)










# Нехай у вас є змінні, які приймають ім'я та прізвище студента, номер його курсу. Створіть функцію, яка виведе значення цих змінних на екран. При цьому нехай прізвище виводиться у верхньому регістрі, а ім'я - тільки перша буква.

# Вхідні дані:
# Shelder 
# Tomas 
# 5

# Вихідні дані:
# SHELDER 
# T
# 5


# def print_studet_info(surname, name, course):
#     print(surname.upper())
#     print(name[0])
#     print(course)



# print_studet_info("Shelder", "Tomas", 5)




# Напишіть функцію min4(a, b, c, d), яка обчислює мінімум чотирьох чисел, яка не містить інструкції if, а використовує стандартну функцію min від двох чисел. Вважайте чотири цілих числа і виведіть їх мінімум.


# def min4(a, b, c, d):
#     return min(a, b, c, d)

# print(min4(1, 5, -56, 100))






# Нехай у вас є словник, в якому як ключі зберігаються імена користувачів, а як значення - їх вік. Створіть функцію, яка виведе всі пари ключ-значення у вигляді кортежу.





# def name_age_tuples(users):
#     return tuple(users.items())

# users = {"Ivan": 20, "Max": 15}
# print(name_age_tuples(users))



# Зробіть функцію, яка параметром прийматиме рядок і повертатиме кортеж її символів.



# def string_tuple(s):
#     return tuple(s)

# print(string_tuple("Hello"))




