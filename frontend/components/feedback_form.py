import streamlit as st
import requests
import os

BACKEND = f"http://{os.getenv('BACKEND_HOST', '127.0.0.1')}:{os.getenv('BACKEND_PORT', '8000')}"

def render():
    st.subheader("Citizen Feedback")
    name = st.text_input("Your Name")
    category = st.selectbox("Category", ["Water", "Energy", "Waste", "Roads", "Other"])
    message = st.text_area("Describe the issue or suggestion")
    if st.button("Submit"):
        payload = {"name": name, "category": category, "message": message}
        r = requests.post(f"{BACKEND}/feedback/submit", json=payload)
        if r.ok:
            st.success("Feedback submitted!")
        else:
            st.error(f"Error: {r.text}")
