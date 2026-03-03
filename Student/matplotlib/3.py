import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 200)
y = np.sqrt(25 - x**2)

plt.plot(x, y)
plt.legend()
plt.xlabel('x')
plt.ylabel('y')



plt.grid()
plt.show()