from fastapi import FastAPI
from app.endpoints import log_analysis

app = FastAPI()

app.include_router(log_analysis.router, prefix="/logs", tags=["Log Analysis"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Logs Processing API"}
