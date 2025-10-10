# lst = [1, 6, 2, 4, 5, 7]

# for i in lst:
#     if i % 2 == 0:
#         print(i)


# lst = ["hello", "python", "world", "banana", "cat"]

# for i in lst:
#     if len(i) > len(lst[0]):
#         print(i)

# rot = []
# lst = ["level", "python", "radar", "hello", "madam"]

# for i in lst:
#     if i == i[::-1]:
#         rot.append(i)
# print(rot)

# r = []
# lst = [1, 2, 3, 4, 5]
# for i in lst:
#     if i % 2 == 0:
#         r.append(i + 1)
#     else:
#         r.append(i - 1)
# print(r)
        





# import random

# for i in range(1, 6):
#     user_door = int(input("Виберіть двері: "))
#     danger_door = random.randint(1, 3)
#     if user_door == danger_door:
#         print("ви програли")
#         break
#     else:
#         print("ви перейшли в насиупну кімнату")





# k = 50
# for i in range(k):
#     if str(i) == str(i)[::-1]:
#        print(i)

    
  

# import random
# for i in range(10):
#     print(random.randint(1, 100))
    

# y = 9
# k = 3
# day = 1
# while k < y:
#     k *= 1.1
#     day += 1

# print(day)





# rez = []
# nums = [2, 3, 4]
# st = [3, 2, 1]
# for i in range(len(nums)):
#     rez.append(nums[i] ** st[i])
# print(rez)



# Створити список материків західної півкулі. Доповнити список материками зі східної півкулі. Відсортувати материки за алфавітом і вивести на екран





# east = ["E", "AF", "A"]
# west = ["NA", "SA"]

# all_con = east + west
# all_con.sort()
# print(all_con)







# rez = ['c', 'a', 'b']
# chars = []
# chars.extend(rez)
# print(chars)  



# lst = [22, 54, 62, 73, 23]
# suma = sum(lst)
# print(suma)



# lst = ['cat', 'window', 'defenestrate', 'apple', 'banana', 'orange']
# last = lst.pop(5)
# print(last)



# lst = [5, 3, 7, 91]
# a = sum(lst) / len(lst)
# print(a)





# 2






# students = {"Петренко": 3, "Іваненко": 4, "Сидоренко": 5, "Семеренко": 2, "Козленко": 4}
# for key, value in students.items():
#    print(key, value)
            


# students = {"Петров": 3, "Іванов": 4, "Сидоров": 5, "Смирнов": 2, "Козлов": 4}
# top_students = {}

# for name, grade in students.items():
#     if grade >= 4:
#         top_students[name] = grade
# print(top_students)
            
            
            
            
            
            
          
# temperatures = {
#     'Київ': 25,
#     'Львів': 20,
#     'Одеса': 28,
#     'Харків': 22,
#     'Дніпро': 24
# }
# a = sum(temperatures.values()) / len(temperatures)
# print(a)



# users = {
#     'john': 'password123',
#     'alice': 'alice2022',
#     'bob': 'bobiscool',
#     'emma': 'emma1234',
#     'david': 'davidPassword'
# }


# login = input("Введіть логін: ")
# password = input("Введіть пароль: ")

# if login in users and users[login] == password:
#     print("ви зареєстровані")
# else:
#     print("невірний пароль або логін")



# nums = {'a': 3, 'b': 2, 'c': 3, 'd': 1}
# for key, value in nums.items():
#     if value == 3:
#         print(key)

# rez = []
# dct = { 'x': '1', 'y': '2', 'z': '3', 'v': '5'}
# for key, value in dct.items():
#     rez.append(int(key * value))
# print(rez)



# text = "programming"
# vowels = "aieou"

# count = {}
# for i in vowels:
#     count[i] = text.count(i)
# print(count)