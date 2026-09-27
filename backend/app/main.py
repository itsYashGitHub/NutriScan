from fastapi import FastAPI

app = FastAPI(title="NutriScan API")

@app.get("/")
def root():
    return {"message": "NutriScan API is running"}

@app.get("/health")
def health():
    return {"status": "ok"}