from fastapi import FastAPI
from your_service.application.health import health_status

app = FastAPI(title="your-service")

@app.get("/health", tags=["operations"])
def health() -> dict[str, str]:
    return health_status()
