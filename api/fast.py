from fastapi import FastAPI
import pandas as pd
import numpy as np

from taxifare.predict import load_model, prediction
# Here you can replace pickle with joblib or cloudpickle
from joblib import load



model_path = 'models/linreg_pipeline.joblib'

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Welcome to the TaxiFare API"}


@app.get("/predict")
def predict(
    pickup_datetime: str,
    pickup_longitude: float,
    pickup_latitude: float,
    dropoff_longitude: float,
    dropoff_latitude: float,
    passenger_count: int
    ):
    X = pd.DataFrame([{
        'pickup_datetime': pickup_datetime,
        'pickup_longitude': pickup_longitude,
        'pickup_latitude': pickup_latitude,
        'dropoff_longitude': dropoff_longitude,
        'dropoff_latitude': dropoff_latitude,
        'passenger_count': passenger_count
    }])


    model = load_model(model_path=model_path)
    fare = prediction(model, X)
    return {"fare": float(fare[0])}
