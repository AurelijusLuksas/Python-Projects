import pandas as pd
import matplotlib.pyplot as plt

def read_parquet_file(file_path):
    df = pd.read_parquet(file_path)
    return df

df = read_parquet_file(r'4 uzduotis\yellow_tripdata_2020-01.parquet')
plt.figure(figsize=(15,9))
plt.scatter(df['passenger_count'], df['trip_distance'], alpha=0.5)
plt.title('Passenger Count compared to Trip Distance')
plt.xlabel('Passenger Count')
plt.ylabel('Trip Distance')
plt.show()

# Keleivių skaičiaus ir kelionės atstumo palyginimas.