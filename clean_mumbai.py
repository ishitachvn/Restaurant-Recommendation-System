import pandas as pd

mumbai = pd.read_csv(
    "dataset/mumbai.csv",
    sep="|"
)

# Select useful columns
mumbai = mumbai[
    [
        "NAME",
        "CUSINE_CATEGORY",
        "RATING",
        "PRICE",
        "REGION",
        "CITY"
    ]
]

# Rename columns to match your project
mumbai.columns = [
    "restaurant name",
    "cuisines type",
    "rate (out of 5)",
    "avg cost (two people)",
    "area",
    "city"
]

# Add restaurant type placeholder
mumbai["restaurant type"] = "Restaurant"

# Reorder columns
mumbai = mumbai[
    [
        "restaurant name",
        "restaurant type",
        "cuisines type",
        "rate (out of 5)",
        "avg cost (two people)",
        "area",
        "city"
    ]
]

# Remove missing values
mumbai.dropna(inplace=True)

mumbai.to_csv(
    "dataset/mumbai_cleaned.csv",
    index=False
)

print(mumbai.head())
print("\nShape:", mumbai.shape)