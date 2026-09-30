# ⚡ ServiceFlow AI

[![Python Version](https://img.shields.io/badge/python-3.12%2B-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-009688.svg)](https://fastapi.tiangolo.com/)
[![LangChain](https://img.shields.io/badge/LangChain-Orchestration-orange.svg)](https://www.langchain.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**ServiceFlow AI** is an intelligent triage and dispatch engine designed for automating inbound service requests through advanced AI-powered analysis and structured data extraction.

---

## ✨ Features

* **Intelligent Triage:** Leverages LLM-driven structured output to automatically categorize, prioritize, and route incoming requests.
* **API-First Design:** Built with FastAPI for high-performance, asynchronous integration into existing tech stacks.
* **Extensible Architecture:** Designed with modular components for seamless integration of custom agents and automated workflows.

---

## 🛠️ Tech Stack

* **Framework:** FastAPI & Uvicorn
* **AI & Orchestration:** LangChain, OpenAI API
* **Language:** Python 3.12+

---

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone GitHub repo
cd serviceflow-ai
```

### 2. Setup Environment

Create and activate a virtual environment, then install the dependencies:

```Bash
python3 -m venv venv
source venv/bin/activate
pip install fastapi uvicorn langchain langchain-openai pydantic python-dotenv
```

### 3. Configure Environment Variables

Create a .env file in the root directory and add your OpenAI API key:

```Code snippet
OPENAI_API_KEY=your_openai_api_key_here
```

### 4. Run the Server

Start the FastAPI development server:

```Bash
uvicorn main:app --reload --port 8000
```

### 5. Test the API

Send a sample service request payload to test the triage engine:

```Bash
curl -X POST [http://127.0.0.1:8000/triage](http://127.0.0.1:8000/triage) \
  -H "Content-Type: application/json" \
  -d '{"request_text": "The main payment gateway is throwing 500 errors for all users."}
```
