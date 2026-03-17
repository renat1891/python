import pandas as pd


df = pd.read_csv("python\Student\panda\wfp_food_prices_ukraine.csv")
# print(df.head(20))
df.tail(20)
df.info()
print(df.describe())