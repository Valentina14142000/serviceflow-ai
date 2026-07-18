import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from app.schemas.triage import TriageRequest, TriageResponse

# Load environment variables from .env file
load_dotenv()

# Initialize the model (it will now look for OPENAI_API_KEY in the environment)
llm = ChatOpenAI(model="gpt-4o", temperature=0)

# Bind the schema to the model
structured_llm = llm.with_structured_output(TriageResponse)

def run_triage(request: TriageRequest) -> TriageResponse:
    prompt = f"You are an expert dispatcher. Analyze the request: '{request.raw_text}'"
    return structured_llm.invoke(prompt)