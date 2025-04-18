import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv("Trips_by_Distance.csv")

# Filter dates where trips > 10 million
df_10_25 = df[df['Number of Trips 10-25'] > 10_000_000]
df_50_100 = df[df['Number of Trips 50-100'] > 10_000_000]

# Extract just dates (if you need them)
dates_10_25 = df_10_25['Date']
dates_50_100 = df_50_100['Date']

# Print counts and sample dates
print(f"Dates with >10M trips (10-25 miles): {len(dates_10_25)}")
print(dates_10_25.head())

print(f"\nDates with >10M trips (50-100 miles): {len(dates_50_100)}")
print(dates_50_100.head())

# Convert 'Date' to datetime format for better plotting
df_10_25['Date'] = pd.to_datetime(df_10_25['Date'])
df_50_100['Date'] = pd.to_datetime(df_50_100['Date'])

# --- Plotting ---

plt.figure(figsize=(14, 6))

# Scatterplot for 10-25 mile trips
plt.subplot(1, 2, 1)
plt.scatter(df_10_25['Date'], df_10_25['Number of Trips 10-25'], color='blue', alpha=0.6)
plt.title('Trips (10-25 miles) > 10M')
plt.xlabel('Date')
plt.ylabel('Number of Trips')
plt.xticks(rotation=45)
plt.grid(True)

# Scatterplot for 50-100 mile trips
plt.subplot(1, 2, 2)
plt.scatter(df_50_100['Date'], df_50_100['Number of Trips 50-100'], color='green', alpha=0.6)
plt.title('Trips (50-100 miles) > 10M')
plt.xlabel('Date')
plt.ylabel('Number of Trips')
plt.xticks(rotation=45)
plt.grid(True)

plt.tight_layout()
plt.show()



