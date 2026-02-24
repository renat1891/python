import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-20, 20, 200)
y = np.sin(x)
y2 = x ** 2
print(x)
print(y)

plt.plot(x, y, color='blue', label='y = sin(x)')
plt.plot(x, y2, color='red', linestyle='dashed', label='y = x^2')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()