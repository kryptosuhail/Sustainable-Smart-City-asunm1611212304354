import pandas as pd
import numpy as np

def detect_anomalies(df: pd.DataFrame, z_threshold: float = 2.0):
    vals = df['value'].astype(float).values
    mu, sigma = np.mean(vals), np.std(vals) if np.std(vals) != 0 else 1.0
    z = np.abs((vals - mu) / sigma)
    anomalies = (z > z_threshold)
    df_out = df.copy()
    df_out['z_score'] = z
    df_out['is_anomaly'] = anomalies
    return df_out
