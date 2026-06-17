import pandas as pd

data = pd.read_csv("dataset/zomato.csv")

print("First 5 Rows:")
print(data.head())

print("\nColumns:")
print(data.columns)

print("\nShape:")
print(data.shape)

print("\nMissing Values:")
print(data.isnull().sum())