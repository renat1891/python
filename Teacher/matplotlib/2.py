import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)

fig, ax = plt.subplots(figsize=(4, 4), constrained_layout=True)
fig, bx = plt.subplots(figsize=(8, 4), constrained_layout=True)

ax.plot(x, np.sin(x), 
        color="blue", 
        linewidth=2, 
        marker="o",
        label="sin(x)")

bx.plot(x, np.cos(x), 
        color="green", 
        linestyle="--", 
        label="cos(x)")

ax.set_title("Sin and Cos")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()
ax.grid(True)

plt.show()