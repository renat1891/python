import numpy as np
import matplotlib.pyplot as plt


temp = np.random.randint(-20, 35, 365)

summer = temp[151:243]
avg_summer = np.mean(summer)
freeze = np.sum(temp < 0)


print(avg_summer)
print(freeze)


plt.plot(temp)
plt.xlabel("day")
plt.ylabel("temp")
plt.show()