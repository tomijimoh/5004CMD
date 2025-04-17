import pandas as pd 
from sklearn.linear_model import LinearRegression 
from sklearn.model_selection import train_test_split 
from sklearn.metrics import mean_squared_error, r2_score

# Load the data
df_trips = pd.read_csv("Trips_by_Distance.csv")

# Check for correct column names
print(df_trips.columns)  # Run this once to verify

X = df_trips[
    [
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
]

# Fill missing values in features
X = X.fillna(X.mean())

# Target assignment: define y first, then fill missing
y = df_trips['Population Not Staying at Home']
y = y.fillna(y.mean())

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", round(mse))

r2 = r2_score(y_test, y_pred)
print("R² Score:", round(r2, 4))
