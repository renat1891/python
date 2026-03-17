import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('python/Teacher/pandas/temp.csv')

print(df.head())
print(df.tail())

plt.plot(df['Month'], df['AvgTemp'])
plt.xlabel('Month')
plt.ylabel('Average Temperature')
plt.title('Average Temperature over Months')
plt.show()

