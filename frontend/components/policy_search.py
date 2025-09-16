import streamlit as st
import requests
import os

BACKEND = f"http://{os.getenv('BACKEND_HOST', '127.0.0.1')}:{os.getenv('BACKEND_PORT', '8000')}"

def render():
    st.subheader("Policy Summarization & Vector Search (Demo)")
    text = st.text_area("Paste a policy paragraph to summarize")
    if st.button("Summarize"):
        r = requests.post(f"{BACKEND}/policy/summarize", json={"text": text})
        if r.ok:
            st.write(r.json().get("summary"))
        else:
            st.error(f"Error: {r.text}")

    st.markdown("---")
    st.caption("Vector search (offline in-memory index)")
    with st.form("vec_form"):
        upsert_text = st.text_area("Upsert: text to store as a chunk")
        upsert_id = st.text_input("Chunk ID", value="chunk-1")
        query_text = st.text_input("Query text", value="policy")
        submitted = st.form_submit_button("Run Demo")
        if submitted:
            if upsert_text.strip():
                requests.post(f"{BACKEND}/vector/upsert", json={"id": upsert_id, "text": upsert_text})
                st.success("Upserted.")
            if query_text.strip():
                r = requests.post(f"{BACKEND}/vector/query", json={"text": query_text, "top_k": 3})
                st.json(r.json())
