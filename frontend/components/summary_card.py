import streamlit as st

def metric_card(title: str, value: str):
    st.markdown(
        f"""
        <div style="padding: 16px; border-radius: 16px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
          <div style="font-size: 14px; opacity: 0.7;">{title}</div>
          <div style="font-size: 28px; font-weight: 700;">{value}</div>
        </div>
        """,
        unsafe_allow_html=True
    )
