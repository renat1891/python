import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('python/Teacher/pandas/wfp_food_prices_ukraine.csv')

# print(df.head(20))
# df.info()
# print(df.describe())
df_lviv = df[(df["mktname"] == "Lviv") & (df["category"] == "oil and fats") & (df["unit"] == "KG")]
print(df_lviv)
plt.plot(df_lviv['date'], df_lviv['price'])
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Price of oil and fats in Lviv over time')
plt.xticks(rotation=45)
plt.show()


