import streamlit as st
import requests
import os

BACKEND = f"http://{os.getenv('BACKEND_HOST', '127.0.0.1')}:{os.getenv('BACKEND_PORT', '8000')}"

def render():
    st.subheader("Eco Tips")
    topic = st.text_input("Topic (e.g., energy, water, waste)", value="energy")
    if st.button("Get Tip"):
        r = requests.get(f"{BACKEND}/eco/tips", params={"topic": topic})
        if r.ok:
            data = r.json()
            st.info(data.get("tip"))
        else:
            st.error(f"Error: {r.text}")
