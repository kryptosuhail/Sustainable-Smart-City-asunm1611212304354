# Sustainable Smart City Assistant – Starter

This is a **minimal, runnable skeleton** for the project with:
- FastAPI backend (`app/`)
- Streamlit dashboard (`frontend/`)
- Offline fallbacks for IBM Watsonx Granite and Pinecone so you can run right away.

## 1) Create a virtual environment & install
```bash
# Windows (PowerShell)
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt

# macOS / Linux
python3.11 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 2) Create `.env`
Copy `.env.example` to `.env` and fill keys later. You can run without keys thanks to offline fallbacks.

## 3) Run backend + frontend (two terminals)
```bash
# Terminal 1
uvicorn app.main:app --reload

# Terminal 2
streamlit run frontend/smart_dashboard.py
```

Open the Streamlit UI at the URL printed in terminal (likely http://localhost:8501).

## 4) Sample data
- `data/sample_kpi.csv` for Forecast + Anomaly demos.

## Notes
- Real IBM Watsonx Granite + Pinecone support is wired via env keys. Without keys, the app returns demo responses.
