import streamlit as st
import requests
import os

BACKEND = f"http://{os.getenv('BACKEND_HOST', '127.0.0.1')}:{os.getenv('BACKEND_PORT', '8000')}"

def render():
    st.subheader("Chat Assistant")
    prompt = st.text_area("Ask anything about sustainability, city governance, etc.")
    if st.button("Ask"):
        if not prompt.strip():
            st.warning("Please type a question.")
        else:
            r = requests.post(f"{BACKEND}/chat/ask", json={"prompt": prompt})
            if r.ok:
                st.success("Response:")
                st.write(r.json().get("reply"))
            else:
                st.error(f"Error: {r.text}")
