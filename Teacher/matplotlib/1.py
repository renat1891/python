import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-20, 20, 200)
y = np.sin(x)
y2 = x ** 2
print(x)
print(y)

plt.plot(x, y, color='blue', label='y = sin(x)')
plt.plot(x, y2, color='red',   label='y = x^2', alpha=0.3, linewidth=10)
#  color - колір лінії
#  label - назва лінії для легенди
# alpha - прозорість лінії (0 - повністю прозора, 1 - повністю непрозора)
# linewidth - товщина лінії
# marker - маркер для точок (наприклад, 'o' - круг, 's' - квадрат, '^' - трикутник)
# linestyle - стиль лінії (наприклад, '-' - суцільна, '--' - пунктирна, '-.' - точково-пунктирна, ':' - пунктирна)
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()