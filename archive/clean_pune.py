import pandas as pd

pune = pd.read_csv("dataset/pune.csv")

# Select useful columns
pune = pune[
    [
        "Restaurant_Name",
        "Cuisines",
        "Ratings_out_of_5",
        "Charges_for_two",
        "Locality"
    ]
]

# Rename columns
pune.columns = [
    "restaurant name",
    "cuisines type",
    "rate (out of 5)",
    "avg cost (two people)",
    "area"
]

# Add city column
pune["city"] = "Pune"

# Add restaurant type placeholder
pune["restaurant type"] = "Restaurant"

# Clean cost column
pune["avg cost (two people)"] = (
    pune["avg cost (two people)"]
    .astype(str)
    .str.replace("₹", "", regex=False)
    .str.replace(",", "", regex=False)
)

# Convert to numeric
pune["avg cost (two people)"] = pd.to_numeric(
    pune["avg cost (two people)"],
    errors="coerce"
)

pune["rate (out of 5)"] = pd.to_numeric(
    pune["rate (out of 5)"],
    errors="coerce"
)

# Remove missing values
pune.dropna(inplace=True)

# Reorder columns
pune = pune[
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

pune.to_csv(
    "dataset/pune_cleaned.csv",
    index=False
)

print(pune.head())
print("\nShape:", pune.shape)