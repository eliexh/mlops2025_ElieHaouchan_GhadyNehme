import pandas as pd
import joblib
from pathlib import Path
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error

def train_models(feature_path: str = "data/features_train.csv"):
    df = pd.read_csv(feature_path)
    X = df[['passenger_count', 'hour', 'day_of_week', 'dist_km']]
    y = df['trip_duration']

    m1 = Ridge().fit(X, y)
    m2 = RandomForestRegressor(n_estimators=50, max_depth=10).fit(X, y)

    preds1 = m1.predict(X)
    preds2 = m2.predict(X)

    mse1 = mean_squared_error(y, preds1)
    mse2 = mean_squared_error(y, preds2)

    best_model = m1 if mse1 < mse2 else m2
    best_name = "ridge" if mse1 < mse2 else "random_forest"

    Path("models").mkdir(exist_ok=True)
    model_path = "models/best_model.joblib"
    joblib.dump(best_model, model_path)

    print(f"Training complete. Best model: {best_name} (MSE: {min(mse1, mse2)})")
