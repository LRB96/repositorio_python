import pandas as pd

df = pd.read_csv("players_20.csv")
print(df.head())
print(df.shape)
print(df.columns.values)
print("\n")
print(df.describe())
