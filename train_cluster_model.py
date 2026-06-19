import pandas as pd
import joblib

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Load dataset
data = pd.read_csv("dataset/cleaned_zomato.csv")

# Keep useful columns
model_data = data[
    [
        "restaurant type",
        "cuisines type",
        "rate (out of 5)",
        "avg cost (two people)",
        "area"
    ]
].copy()

# Encode text columns
encoders = {}

for column in [
    "restaurant type",
    "cuisines type",
    "area"
]:

    encoder = LabelEncoder()

    model_data[column] = encoder.fit_transform(
        model_data[column]
    )

    encoders[column] = encoder

# Scale features
scaler = StandardScaler()

scaled_data = scaler.fit_transform(model_data)

# Train K-Means
kmeans = KMeans(
    n_clusters=4,
    random_state=42,
    n_init=10
)

kmeans.fit(scaled_data)

# Save model
joblib.dump(
    kmeans,
    "models/restaurant_clusters.pkl"
)

# Save scaler
joblib.dump(
    scaler,
    "models/scaler.pkl"
)

# Save encoders
joblib.dump(
    encoders,
    "models/encoders.pkl"
)

print("Model trained successfully!")

print(
    data.assign(
        cluster=kmeans.labels_
    )[["restaurant name", "cluster"]].head(20)
)