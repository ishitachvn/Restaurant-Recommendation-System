import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load cleaned dataset
data = pd.read_csv("dataset/cleaned_zomato.csv")

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

def recommend(restaurant_name):
    restaurant_name = restaurant_name.lower().strip()

    matches = data[
        data["restaurant name"].str.lower().str.strip().str.contains(
            restaurant_name,
            na=False
        )
    ]

    if matches.empty:
        return []

    idx = matches.index[0]

    similarity_scores = list(enumerate(similarity[idx]))

    sorted_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    recommendations = []

    for i in sorted_scores:

        restaurant = data.iloc[i[0]]["restaurant name"]

        if restaurant == data.iloc[idx]["restaurant name"]:
            continue

        recommendations.append(restaurant)

        if len(recommendations) == 5:
            break

    return recommendations