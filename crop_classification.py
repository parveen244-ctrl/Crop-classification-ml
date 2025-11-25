import pandas as pd

# Load dataset
df = pd.read_csv("Crop_recommendation.csv")

# Basic information
print("First 5 rows:")
print(df.head())

print("\nShape of dataset:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nMissing values:")
print(df.isnull().sum())

# Example prediction (using mode)
print("\nMost frequent crop in dataset:")
print(df['label'].mode()[0])
