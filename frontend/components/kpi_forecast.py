import streamlit as st
import requests
import os

BACKEND = f"http://{os.getenv('BACKEND_HOST', '127.0.0.1')}:{os.getenv('BACKEND_PORT', '8000')}"

def render():
    st.subheader("KPI Forecast")
    file = st.file_uploader("Upload CSV with columns: date,value", type=["csv"])
    if st.button("Forecast Next Value"):
        if file is None:
            st.warning("Please upload a CSV.")
        else:
            r = requests.post(f"{BACKEND}/kpi/forecast", files={"file": file})
            if r.ok:
                st.success(f"Forecast: {r.json().get('forecast_next')}")
            else:
                st.error(f"Error: {r.text}")
