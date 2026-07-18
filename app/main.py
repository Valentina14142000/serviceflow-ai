from fastapi import FastAPI, HTTPException
from app.schemas.triage import TriageRequest, TriageResponse
from app.services.triage_agent import run_triage

app = FastAPI(title="ServiceFlow AI", version="1.0.0")

@app.get("/")
async def root():
    return {"message": "ServiceFlow AI is running"}

@app.post("/triage", response_model=TriageResponse)
async def triage_request(request: TriageRequest):
    try:
        # Call the agent service to process the triage
        result = run_triage(request)
        return result
    except Exception as e:
        # Catch any errors (e.g., API key issues, model timeouts)
        raise HTTPException(status_code=500, detail=f"Triage failed: {str(e)}")