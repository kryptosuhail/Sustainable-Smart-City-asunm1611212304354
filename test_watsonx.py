from app.core.config import get_settings
import requests

settings = get_settings()

def test_iam_token():
    """Check if IBM API key works by getting IAM token."""
    url = "https://iam.cloud.ibm.com/identity/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {
        "apikey": settings.WATSONX_API_KEY,
        "grant_type": "urn:ibm:params:oauth:grant-type:apikey"
    }
    resp = requests.post(url, headers=headers, data=data)
    print("IAM token status:", resp.status_code)
    print(resp.json())
    return resp.json().get("access_token")

def test_granite_chat(prompt="Hello Watsonx!"):
    """Send a test prompt to Granite LLM."""
    token = test_iam_token()
    if not token:
        print("❌ Failed to get IAM token.")
        return

    url = f"{settings.WATSONX_URL}/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": settings.WATSONX_MODEL_ID,
        "project_id": settings.WATSONX_PROJECT_ID,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 50
    }

    resp = requests.post(url, headers=headers, json=payload)
    print("Granite status:", resp.status_code)
    print(resp.json())

if __name__ == "__main__":
    test_granite_chat("Give me one eco-friendly tip for saving water.")
