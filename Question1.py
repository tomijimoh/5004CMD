import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv("trips_by_distance.csv")

df = df.fillna(df.mean(numeric_only = True)).dropna()

# Average weekly number of short-distance travellers
weekly_short_trips = df.groupby('Week')[['Number of Trips <1', 'Number of Trips >=500']].mean()
print(weekly_short_trips)


total_staying_home = df['Population Staying at Home'].mean()
# print(f"Total people staying at home: {total_staying_home:,.0f}")

weekly_avg = df.groupby('Week')['Population Staying at Home'].mean()
print(weekly_avg, "Weekly average")

distance_cols = [
    'Number of Trips <1', 
    'Number of Trips 1-3', 
    'Number of Trips 3-5',
    'Number of Trips 5-10', 
    'Number of Trips 10-25', 
    'Number of Trips 25-50',
    'Number of Trips 50-100', 
    'Number of Trips 100-250',
    'Number of Trips 250-500',
    'Number of Trips >=500'
]

# Total number of trips by distance
trip_totals = df[distance_cols].sum()


print("Total number of trips by distance range:\n", trip_totals)
# define midpoint distances for each grouped mile
midpoints = [0.5, 2, 4, 7.5, 17.5, 37.5, 75, 175, 375, 500]

# calculate weighted average distance
weighted_avg_distance = (trip_totals * midpoints).sum() / df['Population Not Staying at Home'].sum()

print ("Average miles traveled per week",weighted_avg_distance)

# Graph for staying at home
plt.figure(figsize=(10, 5))
plt.plot(home_week_average['Week'], home_week_average['Population Staying at Home'], color='orange', linestyle= '-')
plt.title('Average Weekly Population Staying at Home')
plt.xlabel('Week')
plt.ylabel('Number of People')
plt.grid(True)

plt.savefig("weekly_home_avg.png")

# Graph for distance travelled
plt.figure(figsize=(12, 6))
total_trips.plot(kind='bar', color='orange')
plt.title('Trip Distribution by Distance')
plt.xlabel('Distance Range (miles)')
plt.ylabel('Number of Trips')
plt.xticks(ticks=range(len(distance_column)), labels=distance_column, rotation=45)
plt.tight_layout()
plt.savefig("trip_distance_distribution.png")

