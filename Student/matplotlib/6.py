import numpy as np
import matplotlib.pyplot as plt

x = np.random.default_rng(0).normal(loc=10, scale=15, size=1000000)

fig, ax = plt.subplots(figsize=(8, 4), constrained_layout=True)
ax.hist(x, bins=10)

ax.grid(True)

plt.show()
