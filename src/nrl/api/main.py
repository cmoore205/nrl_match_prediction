from fastapi import FastAPI

from nrl.core.config import settings

app = FastAPI(title="NRL Match Prediction API")

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "env": settings.env}