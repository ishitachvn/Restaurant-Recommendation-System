import pandas as pd

# Load final merged dataset
data = pd.read_csv("dataset/final_restaurants.csv")

# Convert cost column to numeric
data["avg cost (two people)"] = (
    data["avg cost (two people)"]
    .astype(str)
    .str.replace("₹", "", regex=False)
    .str.replace(",", "", regex=False)
)

data["avg cost (two people)"] = pd.to_numeric(
    data["avg cost (two people)"],
    errors="coerce"
)

# Convert rating column to numeric
data["rate (out of 5)"] = pd.to_numeric(
    data["rate (out of 5)"],
    errors="coerce"
)

# Remove invalid rows
data.dropna(
    subset=[
        "avg cost (two people)",
        "rate (out of 5)"
    ],
    inplace=True
)


def recommend_restaurants(
    city,
    cuisine,
    budget,
    min_rating,
    restaurant_type
):

    filtered = data[
        (data["city"].str.contains(city, case=False, na=False))
        &
        (data["cuisines type"].str.contains(cuisine, case=False, na=False))
        &
        (data["avg cost (two people)"] <= budget)
        &
        (data["rate (out of 5)"] >= min_rating)
        &
        (
            data["restaurant type"].str.contains(
                restaurant_type,
                case=False,
                na=False
            )
        )
    ]

    filtered = filtered.sort_values(
        by="rate (out of 5)",
        ascending=False
    )

    return filtered[
        [
            "restaurant name",
            "restaurant type",
            "cuisines type",
            "rate (out of 5)",
            "avg cost (two people)",
            "city",
            "area"
        ]
    ].head(10)

