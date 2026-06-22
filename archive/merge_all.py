import pandas as pd

bangalore = pd.read_csv("dataset/bangalore_cleaned.csv")
mumbai = pd.read_csv("dataset/mumbai_cleaned.csv")
pune = pd.read_csv("dataset/pune_cleaned.csv")

combined = pd.concat(
    [bangalore, mumbai, pune],
    ignore_index=True
)

combined.to_csv(
    "dataset/final_restaurants.csv",
    index=False
)

print("Final Dataset Shape:")
print(combined.shape)

print("\nMerge Successful!")