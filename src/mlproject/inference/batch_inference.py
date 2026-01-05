import pandas as pd
import joblib
import numpy as np
import os
from pathlib import Path
from datetime import datetime
from mlproject.features.featurize import haversine

def batch_inference(test_path: str, model_path: str = "models/best_model.joblib"):
    if not os.path.exists(model_path):
        raise FileNotFoundError("Run training first: model artifact missing.")

    model = joblib.load(model_path)
    df = pd.read_csv(test_path)

    df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'])
    df['hour'] = df['pickup_datetime'].dt.hour
    df['day_of_week'] = df['pickup_datetime'].dt.dayofweek
    df['dist_km'] = haversine(df['pickup_latitude'], df['pickup_longitude'],
                              df['dropoff_latitude'], df['dropoff_longitude'])

    X_test = df[['passenger_count', 'hour', 'day_of_week', 'dist_km']]
    preds = model.predict(X_test)

    Path("outputs").mkdir(exist_ok=True)
    date = datetime.now().strftime("%Y%m%d")
    output_path = f"outputs/{date}_predictions.csv"

    out = pd.DataFrame({"id": df.get("id", df.index),
                        "trip_duration_prediction": preds})
    out.to_csv(output_path, index=False)

    print(f"Inference complete. Saved to {output_path}")
