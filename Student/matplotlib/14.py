import numpy as np
import matplotlib.pyplot as plt

steps = np.random.randint(0, 20001, 30)

avg_steps = np.mean(steps)
min_steps = np.min(steps)
max_steps = np.max(steps)
low_days = np.sum(steps < 5000)

print("Середнє:", avg_steps)
print("Мінімум:", min_steps)
print("Максимум:", max_steps)
print("Днів < 5000:", low_days)

plt.bar(range(30), steps)
plt.title("Steps for 30 days")
plt.xlabel("Day")
plt.ylabel("Steps")
plt.show()