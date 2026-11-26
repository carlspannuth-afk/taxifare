import pandas as pd
import numpy as np
# Here you can replace pickle with joblib or cloudpickle
from joblib import load

def load_model(model_path):
    with open(model_path, "rb") as f:
        pipeline = load(f)
    return pipeline

def predict(model, X):
    prediction = model.predict(X)
    return prediction

X_dummy = pd.DataFrame([{
        'pickup_datetime': '2013-07-06 17:18:00 UTC',
        'pickup_longitude': -73.950655,
        'pickup_latitude': 40.783282,
        'dropoff_longitude': -73.984365,
        'dropoff_latitude': 40.769802,
        'passenger_count': 1
}])
model_path = "models/linreg_pipeline.joblib"
model = load_model(model_path)
print(predict(model, X_dummy))
