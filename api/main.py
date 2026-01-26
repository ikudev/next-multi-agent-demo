"""
This is the main entry point for the agent.
It defines the workflow graph, state, tools, nodes and edges.
"""

from typing import List
from langchain.tools import tool
from langchain.agents import create_agent
from copilotkit import CopilotKitMiddleware, CopilotKitState
import logging

logger = logging.getLogger(__name__)

@tool
def get_weather(location: str):
    """
    Get the weather for a given location.
    """
    return f"The weather for {location} is 70 degrees."

class AgentState(CopilotKitState):
    proverbs: List[str]

try:
    agent = create_agent(
        model="gpt-4o-mini",
        tools=[get_weather],
        middleware=[CopilotKitMiddleware()],
        state_schema=AgentState,
        system_prompt="You are a helpful research assistant."
    )
    logger.info("Agent created successfully")
except Exception as e:
    logger.error(f"Error creating agent: {e}")
    agent = None
