import pandas as pd

# Load dataset
data = pd.read_csv("dataset/zomato.csv")

# Select useful columns
data = data[['restaurant name',
             'cuisines type',
             'rate (out of 5)',
             'avg cost (two people)']]

print("Before Cleaning:")
print(data.shape)

# Remove rows with missing values
data.dropna(inplace=True)

print("\nAfter Cleaning:")
print(data.shape)

print("\nMissing Values:")
print(data.isnull().sum())

# Save cleaned dataset
data.to_csv("dataset/cleaned_zomato.csv", index=False)

print("\nCleaned dataset saved successfully!")