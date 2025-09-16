import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

def forecast_next(df: pd.DataFrame, periods: int = 1) -> float:
    # expects 'date' and 'value'
    d = df.copy()
    d['t'] = np.arange(len(d)).reshape(-1, 1)
    y = d['value'].values
    X = d['t'].values.reshape(-1, 1)
    model = LinearRegression().fit(X, y)
    next_t = np.array([[len(d) + periods - 1]])
    return float(model.predict(next_t)[0])
