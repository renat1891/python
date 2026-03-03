import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 1000)
y = np.sin(x) + 0.3 * np.cos(3 * x)

plt.plot(x, y,
         linewidth=2.5,
         linestyle='-.',
         alpha=0.8) 

plt.grid(True)
plt.show()