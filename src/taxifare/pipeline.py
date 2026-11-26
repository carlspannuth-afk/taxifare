import pandas as pd
import numpy as np
import math


# Passenger count pipe
def scale_passenger(p):
    p_min = 0.
    p_max = 8.
    p_scaled = (p - p_min) / (p_max - p_min)
    return p_scaled

def scale_timedelta(timedelta):
    scaled = (timedelta - timedelta_min) / (timedelta_max - timedelta_min)
    return scaled

def scale_distance(dist):
    dist_min = 0
    dist_max = 100
    scaled = (dist - dist_min) / (dist_max - dist_min)
    return scaled

def manhattan_distance_for_pipe(df):
    distance = manhattan_distance_vectorized(df, *lonlat_features)
    return pd.DataFrame({'distance': distance})

def transform_time_features(X: pd.DataFrame) -> pd.DataFrame:
    if isinstance(X, pd.Series):
        X = X.to_frame()

    pickup_dt = pd.to_datetime(X["pickup_datetime"], utc=True)
    timedelta = (pickup_dt - pd.Timestamp('2009-01-01T00:00:00', tz='UTC')) / pd.Timedelta(1, 'D')

    pickup_dt_ny = pickup_dt.dt.tz_convert("America/New_York").dt

    dow = pickup_dt_ny.weekday
    hour = pickup_dt_ny.hour
    month = pickup_dt_ny.month

    hour_sin = np.sin(2 * math.pi / 24 * hour)
    hour_cos = np.cos(2 * math.pi / 24 * hour)

    month_sin = np.sin(2 * math.pi / 12 * month)
    month_cos = np.cos(2 * math.pi / 12 * month)

    return pd.DataFrame({
        'hour_sin': hour_sin,
        'hour_cos': hour_cos,
        'day_of_week': dow,
        'month_sin': month_sin,
        'month_cos': month_cos,
        'timedelta': timedelta
    }, index=X.index)
