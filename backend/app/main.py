from fastapi import FastAPI
from app.api.routes.audit import router as audit_router

app = FastAPI(title="NutriScan API", description="Backend API for the NutriScan food auditing system", version="0.1.0")

app.include_router(audit_router)

@app.get("/")
def root():
    return {"message": "NutriScan API is running"}

@app.get("/health")
def health():
    return {"status": "ok"}