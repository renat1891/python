import numpy as np
import matplotlib.pyplot as plt

# matrix = np.random.randint(1,10, (5,4))
# row_mean = np.mean(matrix, axis=0)
# print(matrix)
# print(row_mean)



matrix = np.random.randint(-20, 40, (12,30))
row_mean = np.mean(matrix, axis=1)
high_temp = np.argmax(row_mean)+1
x = np.arange(1,13)
print(matrix)
print(row_mean)
print(high_temp)

plt.plot(x,row_mean)
plt.show()