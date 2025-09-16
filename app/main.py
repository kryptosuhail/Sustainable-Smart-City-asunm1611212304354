from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.chat_router import router as chat_router
from app.api.eco_tips_router import router as eco_router
from app.api.feedback_router import router as feedback_router
from app.api.policy_router import router as policy_router
from app.api.vector_router import router as vector_router
from app.api.kpi_upload_router import router as kpi_router
from app.api.report_router import router as report_router
from app.api.dashboard_router import router as dashboard_router

app = FastAPI(title="Sustainable Smart City Assistant")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router)
app.include_router(eco_router)
app.include_router(feedback_router)
app.include_router(policy_router)
app.include_router(vector_router)
app.include_router(kpi_router)
app.include_router(report_router)
app.include_router(dashboard_router)

@app.get("/")
def root():
    return {"message": "Backend running. Visit /docs for Swagger."}
