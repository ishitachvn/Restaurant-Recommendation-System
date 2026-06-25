import pandas as pd

data = pd.read_csv(
    "dataset/mumbai.csv",
    sep="|"
)

print(data.columns)
print(data.head())
print(data.shape)