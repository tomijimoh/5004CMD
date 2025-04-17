import pandas as pd

# Load the data
df = pd.read_csv("trips_by_distance.csv")

# Fill missing numeric values, drop any remaining NaNs
# df = df.fillna(df.mean(numeric_only=True)).dropna()

# Filter national-level data
national_only = df[df['Level'] == "National"]

# Extract relevant columns
national_only = national_only[['Number of Trips 10-25', 'Number of Trips 50-100', 'Date']]

# Apply filters
set1 = df[df['Number of Trips 10-25'] > 10_000_000]
set2 = df[df['Number of Trips 50-100'] > 10_000_000]

# No compute() needed — you're already working with Pandas!
print("Set1 sample:\n", len(set1))
print("\nSet2 sample:\n", len(set2))
