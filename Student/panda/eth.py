import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("python\Student\panda\eth_usd_dataset.csv", skiprows=[1])
df.head(10)
df['Day Change'] = df['High'] - df['Low']

df.info()
plt.plot(df["Date"], df["Close"])
plt.show()
print(df["Close"].min())
print(df["Close"].max())
print(df["Close"].mean())
print(df)
print(df["Day Change"].max())
print(df["Day Change"].mean())
print(df["Day Change"].min())