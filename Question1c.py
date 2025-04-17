import dask
import time
import pandas as pd
import dask.dataframe as dd
# import matplotlib.pyplot as plt

# Optional: Disable Arrow-based string handling in Dask
dask.config.set({"dataframe.convert-string": False})

# Simulated processor counts for comparison
n_processors = [10, 20]
n_processors_time = {}

# -------------------------------------------
# 1. Load CSV file with Pandas
# -------------------------------------------
csv_path = "Trips_by_Distance.csv"  # Make sure the file is in the same folder
pdf = pd.read_csv(csv_path)

# -------------------------------------------
# 2. Ensure numeric data types
# -------------------------------------------
for col in ["Number of Trips 10-25", "Number of Trips 50-100"]:
    pdf[col] = pd.to_numeric(pdf[col], errors="coerce")

# Optional: Convert 'Date' to datetime
pdf["Date"] = pd.to_datetime(pdf["Date"], errors="coerce")

# Drop any rows with NaNs after conversion
pdf = pdf.dropna(subset=["Number of Trips 10-25", "Number of Trips 50-100", "Date"])

# -------------------------------------------
# 3. Convert to Dask DataFrame
# -------------------------------------------
dask_df = dd.from_pandas(pdf, npartitions=4)

# -------------------------------------------
# 4. Parallel filtering with timing
# -------------------------------------------
for processor in n_processors:
    print(f"\n=== Simulating {processor} processors ===")
    start_time = time.time()

    # Filter trips > 10 million
    trips_10_25 = dask_df[dask_df["Number of Trips 10-25"] > 1e7][["Date", "Number of Trips 10-25"]].compute()
    trips_50_100 = dask_df[dask_df["Number of Trips 50-100"] > 1e7][["Date", "Number of Trips 50-100"]].compute()

    elapsed = time.time() - start_time
    n_processors_time[processor] = elapsed

    print(f"Trips 10–25 Miles >10M: {len(trips_10_25)} rows")
    print(f"Trips 50–100 Miles >10M: {len(trips_50_100)} rows")
    print(f"Time taken: {elapsed:.2f} seconds")

# -------------------------------------------
# 5. Summary of timings
# -------------------------------------------
print("\n=== Time Summary ===")
for proc, t in n_processors_time.items():
    print(f"{proc} processors (simulated): {t:.2f} seconds")
