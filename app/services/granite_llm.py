# app/services/granite_llm.py

import requests
from app.core.config import get_settings

settings = get_settings()

# Toggle this to True if you don’t have valid IBM credentials
USE_MOCK = True


def _get_iam_token() -> str:
    """Fetch IBM Cloud IAM access token using API key."""
    if USE_MOCK:
        return "mock-token"
    url = "https://iam.cloud.ibm.com/identity/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {
        "apikey": settings.WATSONX_API_KEY,
        "grant_type": "urn:ibm:params:oauth:grant-type:apikey"
    }
    resp = requests.post(url, headers=headers, data=data)
    resp.raise_for_status()
    return resp.json()["access_token"]


def _call_watsonx(prompt: str, max_tokens: int = 200) -> str:
    """Send prompt to Watsonx Granite Chat LLM or return mock response."""
    if USE_MOCK:
        if "Summarize" in prompt:
            return "📘 Mock Summary: This is a short summary of the provided text."
        elif "eco-friendly" in prompt or "eco" in prompt.lower():
            return "🌱 Mock Eco Tip: Turn off the tap while brushing your teeth to save water."
        elif "report" in prompt.lower():
            return "📊 Mock Report: City sustainability is good. Energy usage is stable. Air quality improving."
        else:
            return "🤖 Mock Chatbot: This is a simulated response."

    # --- Real Watsonx call ---
    token = _get_iam_token()
    url = f"{settings.WATSONX_URL}/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": settings.WATSONX_MODEL_ID,
        "project_id": settings.WATSONX_PROJECT_ID,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": max_tokens,
    }

    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    result = response.json()

    return result["choices"][0]["message"]["content"]


# ---- High-level helper functions ---- #

def generate_summary(text: str) -> str:
    return _call_watsonx(
        f"Summarize this smart city policy in 2-3 sentences:\n\n{text}",
        max_tokens=150
    )

def ask_granite(prompt: str) -> str:
    return _call_watsonx(
        f"You are a smart city assistant. Answer this question clearly:\n\n{prompt}",
        max_tokens=200
    )

def generate_eco_tip(topic: str) -> str:
    return _call_watsonx(
        f"Provide one practical eco-friendly tip about {topic}. Keep it short and actionable.",
        max_tokens=100
    )

def generate_city_report(city: str, kpi: dict) -> str:
    return _call_watsonx(
        f"Generate a detailed sustainability report for the city '{city}' "
        f"using these KPIs:\n{kpi}\n\nMake it clear and structured.",
        max_tokens=300
    )
