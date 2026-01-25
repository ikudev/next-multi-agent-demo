from fastapi import FastAPI
from copilotkit import CopilotKitSDK, LangGraphAgent
from copilotkit.integrations.fastapi import add_fastapi_endpoint
import os
import sys
from dotenv import load_dotenv

# Load root .env file
load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env"))

# Add current directory to sys.path to import main
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from main import agent

app = FastAPI()

sdk = CopilotKitSDK(
    agents=[
        LangGraphAgent(
            name="sample_agent",
            graph=agent,
        )
    ]
)

add_fastapi_endpoint(app, sdk, "/api/agent")

@app.get("/api/agent/health")
def health():
    return {"status": "ok"}
