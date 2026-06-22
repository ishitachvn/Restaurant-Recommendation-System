import pandas as pd

bangalore = pd.read_csv("dataset/cleaned_zomato.csv")

bangalore["city"] = "Bangalore"

bangalore.to_csv(
    "dataset/bangalore_cleaned.csv",
    index=False
)

print("Saved successfully!")
print(bangalore.shape)