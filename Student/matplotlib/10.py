import numpy as np
import matplotlib.pyplot as plt

A = np.random.normal(0, 1, 5000)
B = np.random.normal(2, 1, 5000)

plt.hist(A, bins=40, alpha=0.5)
plt.hist(B, bins=40, alpha=0.5)

plt.title("Two Normal Distributions")
plt.show()
