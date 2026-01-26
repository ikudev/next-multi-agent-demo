from fastapi import FastAPI, Request
from copilotkit import CopilotKitSDK, LangGraphAgent
from copilotkit.integrations.fastapi import add_fastapi_endpoint
import os
import sys
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Add current directory to sys.path to import main
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)

app = FastAPI()

@app.get("/api/agent/health")
def health():
    try:
        from main import agent
        agent_loaded = agent is not None
    except Exception as e:
        logger.error(f"Health check failed to import agent: {e}")
        agent_loaded = False

    return {
        "status": "ok" if agent_loaded else "error",
        "agent_loaded": agent_loaded,
        "python_version": sys.version,
        "openai_key_present": "OPENAI_API_KEY" in os.environ
    }

# Initialize SDK
try:
    from main import agent
    if agent:
        sdk = CopilotKitSDK(
            agents=[
                LangGraphAgent(
                    name="sample_agent",
                    id="sample_agent", # Explicitly set the ID
                    graph=agent,
                )
            ]
        )
        add_fastapi_endpoint(app, sdk, "/api/agent")
        logger.info("CopilotKit SDK initialized successfully")
    else:
        logger.error("Agent is None, could not initialize SDK")
except Exception as e:
    logger.error(f"Failed to initialize CopilotKit SDK: {e}")

@app.get("/api/agent/list")
def list_agents():
    """Debug endpoint to see registered agents."""
    return {"agents": [a.id for a in sdk.agents]}
