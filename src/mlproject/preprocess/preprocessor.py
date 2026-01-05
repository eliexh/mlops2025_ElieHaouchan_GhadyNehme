import pandas as pd
from pathlib import Path

def preprocess_data(input_path: str, output_path: str):
    df = pd.read_csv(input_path)

    df = df.dropna()
    df = df[df['passenger_count'] > 0]
    df = df[df['trip_duration'] > 0]
    df = df.drop(columns=['dropoff_datetime'])

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)

    print("Preprocessing complete.")
