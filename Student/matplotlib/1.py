import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-20, 20, 200)
y = np.cos(x)

plt.plot(x, y)
plt.title("y = cos(x)")
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()