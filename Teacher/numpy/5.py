import numpy as np
import matplotlib.pyplot as plt

matrix = np.random.randint(-20, 40, (12,30))
row_mean = np.mean(matrix, axis=1)
high_temp = np.argmax(row_mean)+1
x = np.array(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
print(matrix)
print(row_mean)
print(high_temp)

plt.plot(x,row_mean)
plt.show()