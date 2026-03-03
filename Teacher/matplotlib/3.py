import numpy as np
import matplotlib.pyplot as plt

x = np.random.default_rng(42).normal(loc=0, scale=1, size=1000)

fig, ax = plt.subplots(figsize=(8, 4), constrained_layout=True)
ax.hist(x, bins=10)

ax.grid(True)

plt.show()