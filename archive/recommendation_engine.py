import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load cleaned dataset
data = pd.read_csv("dataset/final_restaurants.csv")


# Create a combined feature column
data["features"] = (
    data["cuisines type"] + " " +
    data["rate (out of 5)"].astype(str) + " " +
    data["avg cost (two people)"].astype(str)
)

print("Features created successfully!\n")
print(data[["restaurant name", "features"]].head())

# Convert text into vectors
vectorizer = TfidfVectorizer()

feature_matrix = vectorizer.fit_transform(data["features"])

print("\nFeature matrix shape:")
print(feature_matrix.shape)

similarity = cosine_similarity(feature_matrix)

print("\nSimilarity matrix shape:")
print(similarity.shape)

def recommend(restaurant_name, city=None):

    restaurant_name = restaurant_name.lower().strip()

    search_data = data

    if city:
        search_data = data[
            data["city"].str.lower() == city.lower()
        ]

    matches = search_data[
        search_data["restaurant name"]
        .str.lower()
        .str.strip()
        .str.contains(
            restaurant_name,
            na=False
        )
    ]

    if matches.empty:
        return []

    idx = matches.index[0]

    similarity_scores = list(
        enumerate(similarity[idx])
    )

    sorted_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    recommendations = []

    for i in sorted_scores:

        restaurant_idx = i[0]

        if restaurant_idx == idx:
            continue

        recommendations.append({
            "restaurant name":
                data.iloc[restaurant_idx]["restaurant name"],

            "cuisines type":
                data.iloc[restaurant_idx]["cuisines type"],

            "rating":
                data.iloc[restaurant_idx]["rate (out of 5)"],

            "cost":
                data.iloc[restaurant_idx]["avg cost (two people)"],

            "city":
                data.iloc[restaurant_idx]["city"]
        })

        if len(recommendations) == 5:
            break

    return recommendations

results = recommend(
    "Hitchki",
    city="Mumbai"
)

for restaurant in results:
    print(restaurant)