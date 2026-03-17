import numpy as np
import matplotlib.pyplot as plt
spend = np.random.randint(0, 2000, (365))
avg = np.mean(spend)
x = np.arange(1, 366)
y = np.full(365, avg)
print(spend)
print(avg)
print(np.sum(spend>1000))
plt.plot(x, spend)
plt.plot(x,y)
plt.show()