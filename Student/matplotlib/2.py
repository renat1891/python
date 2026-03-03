import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 50)
y = np.abs(x)

plt.plot(x, y, label = "abs(x)")
plt.legend()
plt.xlabel('x')
plt.ylabel('y')

x = np.linspace(-10, 10, 50)
y = np.cos(x)
plt.plot(x, y, label="cos(x)")
plt.title("y = cos(x)")
plt.legend()
plt.xlabel('x')
plt.ylabel('y')

x = np.linspace(-10, 10, 50)
y = np.sqrt(x)
plt.plot(x, y, label="sqrt(x)")
plt.legend()
plt.xlabel('x')
plt.ylabel('y')






plt.grid()
plt.show()