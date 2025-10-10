# lst = [1, 2, 6, 7, 8]

# print(sum(lst))


# suma = 0

# lst = [1, 2, 6, 7, 8]

# for i in lst:
#     suma += i
# print(suma)


# lst = [1, 2, 6, 7, 8, 3]

# print(sum(lst)/ len(lst)) 



# lst = [1, 2, 6, 7, 8, 3]

# print(sum(lst[:3]))


# suma = 0

# lst = [1, 2, 6, 7, 8, 3, 9]

# for i in lst:
#     if i % 2 == 1:
#         suma += i
# print(suma)
    




# lst = ["cat", "dog", "bird", "elephant", "lion", "tiger", "giraffe", "monkey", "zebra", "penguin"]

# for word in lst:
#     if "e" == word[2]:
#         print(word)






# import random 

# mnum = random.randint(0, 100)

# while True:
#     user_num = int(input("Введіть число: "))
#     if mnum > user_num:
#         print("Загадане число більше")
#     elif mnum < user_num:
#         print("Загадане число менше")
#     else:
#         print("Ви вгадали число")
#         break







# rez =[]

# lst = ["level", "python", "radar", "hello", "madam"]
# for i in lst:
#     if i == i[::-1]:
#         rez.append(i)
# print(rez)





# rez =[]

# lst = [129, 45, 6, 789]

# n = 10
# for i in lst:
#     if i > n:
#         rez.append(i)
# print(rez)

















# import random 

# mnum = random.randint(0, 100)
# for i in range(1, 8):
#     user_num = int(input(f"спроба {i}: Введи число: "))
#     if mnum == user_num:
#      print("ви вгадали число")
#      break
#     elif mnum > user_num:
#      print("Загадане число більше ")
#     else:
#      print("Загадане число менше")
# else:
#   print("Ти програв")

     
    

# lst = ["hello", "python", "pizza", "house"]
# import random
# secret_word = random.choice(lst)
# guessed_letters = set()
# correct_leters = set()
# while True:
#     letter = (input("Введіть букву: "))
#     if letter in guessed_letters:
#         print(f"Букву {letter} вже вводили")
#         continue
#     guessed_letters.add(letter)
#     if letter in secret_word:
#         correct_leters.add(letter)
#         print(f"Буква {letter} є у слові")
#     else:
#         print(f"букви {letter} немає ц слові")
#     current_state = "".join([ch if ch in correct_leters else "_" for ch in secret_word])
#     print("слово: ", current_state)
#     if set(secret_word) == correct_leters:
#         print("ви відгадали слово")
#         break








# Надрукувати таблицю відповідності між масою у фунтах і масою в кілограмах для значень n фунтів (1 фунт = 453 г) у вигляді таблиці.




# n = 10
# for i in range(1, n + 1):
#     kg = n * 0.453
#     print(n, "фунтів = ", round(kg, 3), "кг")

# print("Введітб послідовність чисел")

# max_num = None

# while True:
#     n = int(input('Введіть чилсо:'))
#     if n == 0:
#         break
#     if max_num is None or n > max_num:
#         max_num = n
    
# print(max_num)  




