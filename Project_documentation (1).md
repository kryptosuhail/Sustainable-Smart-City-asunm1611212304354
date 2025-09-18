Sustainable Smart City Assistant Using Granite LLM Project Documenta
Ɵon 1. Introduc Ɵon  Project Title: Sustainable Smart City Assistant 
Team Members: Rahman Khan .A  Team Members: Sanjai.S  Team Members:
Prajin  Team Members: Sanjairam 2. Project Overview Purpose The
Sustainable Smart City Assistant empowers ci Ɵes and ciƟzens to thrive
in an eco-conscious and connected urban environment. By leveraging IBM
Watsonx Granite LLMs, Pinecone vector database, and real- Ɵme data analy
Ɵcs, it opƟmizes energy, water, and waste usage while providing ac
Ɵonable sustainability insights. For ciƟzens, it delivers policy
summaries, eco- Ɵps, and chatbot support . For oﬃcials, it provides
decision- making insights, anomaly detec Ɵon, KPI forecasƟng, and
sustainability reports . Features  Conversa Ɵonal Chat Assistant --
Natural language Q&A powered by IBM Watsonx Granite.  Policy Summariza
Ɵon -- Converts lengthy government documents into concise, ac Ɵonable
summaries.\
 Eco Tip Generator -- Provides personalized, prac Ɵcal sustainability
advice.  CiƟzen Feedback Loop -- Collects and analyzes public feedback
to guide planning.  KPI Forecas Ɵng -- Predicts trends in air quality,
energy, and green cover.  Anomaly Detec Ɵon -- Flags unusual values in
KPI/sensor data.  Document & Data Search -- Uses Pinecone vector
embeddings for semanƟc retrieval.\
 City Report Generator -- Produces structured sustainability reports. 
MulƟmodal Input -- Accepts PDFs, CSVs, and text ﬁles.  InteracƟve
Dashboard -- Built with Streamlit for a user-friendly interface. 3.
Architecture Frontend (Streamlit)  Provides naviga Ɵon sidebar with
modules: Chat, Policy Summarizer, Eco Tips, KPI & Report Dashboard . 
Visualizes KPIs with metrics, anomaly detec Ɵon ﬂags, and bar charts.\
Backend (FastAPI)  Exposes REST API endpoints for summariza Ɵon, chat,
eco Ɵps, feedback, reports, and vector search.  Fully documented via
Swagger UI (/docs). LLM Integra Ɵon (IBM Watsonx Granite)\
 Uses Granite family of LLMs via IBM Cloud API key authen ƟcaƟon. 
Handles summariza Ɵon, report genera Ɵon, eco-Ɵps, and chat.\
Vector Search (Pinecone)  Sentence-transformer embeddings stored in
Pinecone.  SemanƟc search enables users to query policies and city data
in natural language . ML Modules  ForecasƟng: Uses scikit-learn
regression to project KPIs.  Anomaly Detec Ɵon: IdenƟﬁes unusual KPI
values with threshold and staƟsƟcal methods.

4.  Setup Instruc Ɵons Prerequisites  Python 3.9+  IBM Watsonx API
    key, Project ID, Model ID  Pinecone API key  Virtual environment &
    pip InstallaƟon git clone `<your-repo-url>`{=html} cd
    smartcity-assistant-starter python -m venv .venv
    ..venv`\Scripts`{=tex} acƟvate \# Windows\
    pip install -r requirements.txt

Environment Variables (.env)
WATSONX_API_KEY=pAjcxi3Df0g687V0mCe3_Q8TmRKSDlp9wuIxo52qwNn5
WATSONX_PROJECT_ID=f371addd-61dd-4ﬀ0-882d-571db5a32aea WATSONX_URL
=hƩps://eu-de.ml.cloud.ibm.com
WATSONX_MODEL_ID=ibm/granite-13b-instruct-v2
PINECONE_API_KEY=pcsk_22YGB3_9RY8BMqaUZN55nkxUA7nR7ZyhBnKA1LjW
44XtRpkeo43rcmj2yw4HrPhQfQbafu PINECONE_ENV=us-east-1
INDEX_NAME=smartcity-policies

Running Backend: uvicorn app.main:app --reload Frontend:\
streamlit run frontend/smart_dashboard.py\
5. Folder Structure\
app/ ├── api/ \# FastAPI routers\
├── core/ \# Conﬁg & Pinecone client\
├── services/ \# LLM, embeddings, forecas Ɵng, anomaly detec Ɵon
frontend/\
└── smart_dashboard.py \# Streamlit frontend

6.  Running the Applica Ɵon
7.  Start FastAPI backend → h Ʃp://127.0.0.1:8000/docs\
8.  Start Streamlit frontend → h Ʃp://localhost:8501\
9.  Navigate through:

o 밈밉밊밋밌밍밎및 Chat Assistant

o 궀궔궂궃 Policy Summarizer

o 芢芣 Eco Tips

o 굇굃굈굉굊 KPI Dashboard & City Report

o 굅굃굆 Anomaly Checker

7.  API Documenta Ɵon  POST /chat/ask → Smart city Q&A\
     POST /policy/summarize → Summarize policy text\
     GET /eco/ Ɵps?topic= → Eco Ɵps  POST /report/ → Generate city
    sustainability report\
     POST /vector/upsert → Upload & embed documents\
     GET /vector/search?query= → Search uploaded documents\
     POST /feedback/ → Store ci Ɵzen feedback\

8.  Authen ƟcaƟon  All IBM Watsonx endpoints require IAM token (fetched
    via API key) .  Pinecone requires API key & environment ID.\
     Can extend with JWT/OAuth2 for secure produc Ɵon deployment.\

9.  User Interface\
     Clean Streamlit dashboard with sidebar naviga Ɵon.  KPI visualiza
    Ɵons with cards & bar charts.\
     Tabbed layouts for summaries, eco Ɵps, anomaly detec Ɵon, and
    forecasƟng.

10. TesƟng  Unit Tests for LLM prompt func Ɵons.  API Tests via
    Swagger & Postman.\
     Manual Tes Ɵng for frontend ﬂows.\
     Edge Cases → invalid inputs, large ﬁles, missing creden Ɵals.

11. Future Enhancements  Role-based access control (Admin, Ci Ɵzen,
    Researcher).\
     Real-Ɵme IoT sensor integra Ɵon for KPIs.\
     Geo-mapping dashboard with sustainability layers.  MulƟlingual
    support with IBM Watson Language Translator.
