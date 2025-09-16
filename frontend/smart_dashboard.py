# frontend/smart_dashboard.py
import streamlit as st
import requests
import pandas as pd
import altair as alt

# ----------------- CONFIG -----------------
st.set_page_config(
    page_title="🌇 Smart City Assistant",
    page_icon="🏙️",
    layout="wide"
)

# Change this if your backend runs on a different host/port
backend_url = "http://127.0.0.1:8000"

# Header / Hero
st.markdown(
    """
    <div style="background: linear-gradient(90deg, #FFE6CC 0%, #FDEBD0 50%, #FFF5EA 100%);
                padding:18px; border-radius:12px; margin-bottom:16px;">
        <h1 style="color:#E67E22; margin:0;">🌇 Smart City Assistant</h1>
        <p style="color:#784212; margin:0;">Demo dashboard — sustainability, policy summarization, eco tips and chat (mock mode).</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Sidebar navigation
st.sidebar.markdown("## 🔎 Navigation")
page = st.sidebar.radio("", [
    "🤖 Chat Assistant",
    "📘 Policy Summarizer",
    "🌱 Eco Tips",
    "📊 City Report"
])

# Small helper for calling backend
def post_json(path, payload):
    try:
        r = requests.post(f"{backend_url}{path}", json=payload, timeout=8)
        return r
    except Exception as e:
        st.error(f"Backend not reachable: {e}")
        return None

def get_json(path, params=None):
    try:
        r = requests.get(f"{backend_url}{path}", params=params, timeout=8)
        return r
    except Exception as e:
        st.error(f"Backend not reachable: {e}")
        return None

# ------------- Chat Assistant -------------
if page == "🤖 Chat Assistant":
    st.markdown("<h2 style='color:#E67E22;'>🤖 Chat Assistant</h2>", unsafe_allow_html=True)
    st.write("Ask anything about smart cities (mock responses enabled).")

    chat_input = st.text_input("Your question")
    if st.button("Send"):
        if chat_input.strip():
            resp = post_json("/chat/ask", {"prompt": chat_input})
            if resp is None:
                pass
            elif resp.status_code == 200:
                st.success(resp.json().get("response"))
            else:
                st.error(f"Error {resp.status_code}: {resp.text}")

# ------------- Policy Summarizer -------------
elif page == "📘 Policy Summarizer":
    st.markdown("<h2 style='color:#E67E22;'>📘 Policy Summarizer</h2>", unsafe_allow_html=True)
    st.write("Paste a policy paragraph or long text; click Summarize.")

    text_input = st.text_area("Policy text", height=220)
    if st.button("Summarize"):
        if text_input.strip():
            resp = post_json("/policy/summarize", {"text": text_input})
            if resp is None:
                pass
            elif resp.status_code == 200:
                st.info(resp.json().get("summary"))
            else:
                st.error(f"Error {resp.status_code}: {resp.text}")

# ------------- Eco Tips -------------
elif page == "🌱 Eco Tips":
    st.markdown("<h2 style='color:#E67E22;'>🌱 Eco Tips</h2>", unsafe_allow_html=True)
    topic = st.text_input("Topic (e.g., energy, water, transport):")
    if st.button("Get Tip"):
        if topic.strip():
            resp = get_json("/eco/tips", params={"topic": topic})
            if resp is None:
                pass
            elif resp.status_code == 200:
                st.success(resp.json().get("tip"))
            else:
                st.error(f"Error {resp.status_code}: {resp.text}")

# ------------- City Report -------------
elif page == "📊 City Report":
    st.markdown("<h2 style='color:#E67E22;'>📊 City Report</h2>", unsafe_allow_html=True)
    st.write("Enter city and KPIs and generate a quick sustainability report (mock).")

    with st.form("report_form"):
        col1, col2 = st.columns(2)
        with col1:
            city = st.text_input("City name", "Bengaluru")
        with col2:
            kpi_air = st.text_input("Air Quality", "Moderate")
            kpi_green = st.text_input("Green Cover", "30%")
            kpi_energy = st.text_input("Renewable Energy", "45%")
        submitted = st.form_submit_button("Generate Report")

    if submitted:
        kpi = {"AirQuality": kpi_air, "GreenCover": kpi_green, "RenewableEnergy": kpi_energy}
        resp = post_json("/report/", {"city": city, "kpi": kpi})
        if resp is None:
            pass
        elif resp.status_code == 200:
            st.markdown("### 📝 Generated Report")
            st.write(resp.json().get("report"))
        else:
            st.error(f"Error {resp.status_code}: {resp.text}")

    # KPI cards and example chart
    st.subheader("📈 KPI Overview")
    col1, col2, col3 = st.columns(3)
    col1.metric("Air Quality", kpi_air)
    col2.metric("Green Cover", kpi_green)
    col3.metric("Renewables", kpi_energy)

    df = pd.DataFrame({
        "Category": ["Air Quality", "Green Cover", "Renewables"],
        "Value": [50, int(kpi_green.strip('%')) if isinstance(kpi_green, str) and kpi_green.strip('%').isdigit() else 30, 
                  int(kpi_energy.strip('%')) if isinstance(kpi_energy, str) and kpi_energy.strip('%').isdigit() else 45]
    })
    chart = alt.Chart(df).mark_bar().encode(x="Category", y="Value", color="Category")
    st.altair_chart(chart, use_container_width=True)
