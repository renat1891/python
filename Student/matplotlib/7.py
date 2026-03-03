import numpy as np
import matplotlib.pyplot as plt

# Параметри сфери
r = 1
u = np.linspace(0, 2*np.pi, 100)
v = np.linspace(0, np.pi, 100)

# Сітка кутів
u, v = np.meshgrid(u, v)

# Параметричні рівняння сфери
x = r * np.cos(u) * np.sin(v)
y = r * np.sin(u) * np.sin(v)
z = r * np.cos(v)

# Створення 3D фігури
fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(projection='3d')

# Малюємо поверхню
ax.plot_surface(x, y, z, alpha=0.7)

ax.set_title("3D Sphere")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

plt.show()
