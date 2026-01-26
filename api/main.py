from fastapi import FastAPI
from ag_ui_langgraph import add_langgraph_fastapi_endpoint
from copilotkit import LangGraphAGUIAgent
import os
import sys
import logging
import uvicorn
from dotenv import load_dotenv

# Load root .env file
load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env"))

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Add current directory to sys.path to import main
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)

from agent import agent

app = FastAPI()

@app.get("/agent/health")
def health():
    return {
        "status": "ok",
        "agent_loaded": agent is not None,
        "openai_key_present": "OPENAI_API_KEY" in os.environ
    }

# Using the configuration from the latest documentation
add_langgraph_fastapi_endpoint(
    app=app,
    agent=LangGraphAGUIAgent(
        name="sample_agent",
        description="An example agent to use as a starting point for your own agent.",
        graph=agent,
    ),
    path="/agent",
)

def main():
  """Run the uvicorn server."""
  uvicorn.run(
    "main:app",
    host="0.0.0.0",
    port=8123,
    reload=True,
  )
if __name__ == "__main__":
  main()
