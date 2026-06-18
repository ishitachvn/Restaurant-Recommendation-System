import pandas as pd

# Load dataset
data = pd.read_csv("dataset/cleaned_zomato.csv")


def recommend_restaurants(
    cuisine,
    budget,
    min_rating,
    restaurant_type
):

    filtered = data[
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
            "avg cost (two people)"
        ]
    ].head(10)