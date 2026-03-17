import numpy as np
import matplotlib.pyplot as plt

rate = [40]

for i in range(364):
    change = np.random.uniform(-0.2, 0.2)
    rate.append(rate[-1] + change)

rate = np.array(rate)

avg_rate = np.mean(rate)
max_rate = np.max(rate)
min_rate = np.min(rate)
max_day = np.argmax(rate)
min_day = np.argmin(rate)

increase_days = np.sum(rate[1:] > rate[:-1])

print("Середнє:", avg_rate)
print("Максимум:", max_rate, "день:", max_day)
print("Мінімум:", min_rate, "день:", min_day)
print("Днів росту:", increase_days)

plt.plot(rate)
plt.title("Rate for 365 days")
plt.xlabel("Day")
plt.ylabel("Rate")
plt.show()