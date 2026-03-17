import numpy as np
import matplotlib.pyplot as plt

sales = np.random.randint(50, 500, 365)

avg_sales = np.mean(sales)
max_day = np.argmax(sales)
days_above_avg = np.sum(sales > avg_sales)

print("Середній продаж:", avg_sales)
print("День з максимальним продажем:", max_day)
print("Кількість днів > середнього:", days_above_avg)

plt.plot(sales)
plt.title("Sales for 365 days")
plt.xlabel("Day")
plt.ylabel("Sales")
plt.show()