import numpy as np

# це простий 1d список
# a = np.array([1, 2, 3, 4, 5])
# print(a)

# це 2d список
# b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9.1]])
# print(b)
# print(b.shape)  # виводить розмірність масиву
# print(b.ndim)   # виводить кількість вимірів масиву
# print(b.size)   # виводить загальну кількість елементів у масиві
# print(b.dtype)  # виводить тип даних елементів масиву


# це 3d список
# c = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]])
# print(c)

# створити матрицю з нулями розміром 3 на 3
# zeros_matrix = np.zeros((3, 3))   
# print(zeros_matrix)

# створити матрицю з одиницями розміром 4 на 4
# ones_matrix = np.ones((4, 4))
# print(ones_matrix)

# заповнені 7-ми матриці розміром 4 на 4
# sevens_matrix = np.full((4, 4), 0)
# print(sevens_matrix)

# діапазон від 0 до 9
# range_array = np.arange(10)
# print(range_array)

# діапазон від 1 до 10 з кроком 2
# range_step_array = np.arange(1, 10, 2)
# print(range_step_array)

# це 5 рівновіддалених точок між 0 та 1
# linspace_array = np.linspace(100, 200, 101)
# print(linspace_array)

# 
# b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(b)  # виводить перший рядок
# print(b[0, 0])  # виводить перший елемент першого рядка
# print(b[0]) # виводить перший рядок
# print(b[1, 2])  # виводить третій елемент другого рядка
# print(b[1:, 0:2])  # виводить підмасив з другого та третього рядка та перших двох стовпців
# print(b[b>3])

# a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# print(a + b)  # поелементне додавання
# print(a * b)  # поелементне множення
# print(a / b)  # поелементне ділення
# print(a - b)  # поелементне віднімання

# рандом
# random_array = np.random.rand(3, 3)  # створює 3x3 масив з випадковими числами від 0 до 1
# print(random_array)

# рандомні цілі числа від 0 до 9 у масиві 4x4
# random_int_array = np.random.randint(0, 10, (4, 4))
# print(random_int_array)

b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(b)
print(b.T)  # транспонування матриці
