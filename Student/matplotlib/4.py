import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 200)
y = np.sin(x)

plt.plot(x, y)


x = np.linspace(-5, 5, 200)
y = np.cos(x)

plt.plot(x, y)



x = np.linspace(-5, 5, 200)
y = np.sin(x) * np.cos(x)

plt.plot(x, y)
plt.grid(True)
plt.show()
