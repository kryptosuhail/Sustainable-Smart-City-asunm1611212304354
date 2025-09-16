from fastapi import APIRouter, UploadFile, File
import pandas as pd
from app.services.kpi_file_forecaster import forecast_next
from app.services.anomaly_file_checker import detect_anomalies

router = APIRouter(prefix="/kpi", tags=["kpi"])

@router.post("/forecast")
async def forecast(file: UploadFile = File(...)):
    df = pd.read_csv(file.file)
    yhat = forecast_next(df, periods=1)
    return {"forecast_next": yhat}

@router.post("/anomaly")
async def anomaly(file: UploadFile = File(...)):
    df = pd.read_csv(file.file)
    out = detect_anomalies(df)
    return {"rows": out.to_dict(orient="records")}
