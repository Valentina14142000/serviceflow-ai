from pydantic import BaseModel, Field
from typing import Optional

class TriageRequest(BaseModel):
    raw_text: str = Field(..., description="The original message from the customer")

class TriageResponse(BaseModel):
    issue_type: str = Field(..., description="The category of the issue (e.g., plumbing, HVAC, electrical)")
    urgency_level: int = Field(..., ge=1, le=5, description="Urgency scale from 1 to 5")
    location: Optional[str] = Field(None, description="The customer's address or location")
    summary: str = Field(..., description="A concise professional summary of the request")