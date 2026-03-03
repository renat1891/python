import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(0, 1, 5000)

plt.hist(data, bins=50)
plt.title("Normal(0,1)")
plt.show()

print("Mean:", np.mean(data))
print("Std:", np.std(data))