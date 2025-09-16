import streamlit as st
import requests
import os
import pandas as pd

BACKEND = f"http://{os.getenv('BACKEND_HOST', '127.0.0.1')}:{os.getenv('BACKEND_PORT', '8000')}"

def render():
    st.subheader("Anomaly Checker")
    file = st.file_uploader("Upload CSV with columns: date,value", type=["csv"])
    if st.button("Check Anomalies"):
        if file is None:
            st.warning("Please upload a CSV.")
        else:
            r = requests.post(f"{BACKEND}/kpi/anomaly", files={"file": file})
            if r.ok:
                st.dataframe(pd.DataFrame(r.json().get("rows", [])))
            else:
                st.error(f"Error: {r.text}")
