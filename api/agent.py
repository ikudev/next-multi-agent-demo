from langgraph.graph import END, START, StateGraph
from langgraph.checkpoint.memory import MemorySaver
from langchain_core.messages import SystemMessage, BaseMessage
from langchain.chat_models import init_chat_model
from copilotkit import CopilotKitState
from typing import List

class AgentState(CopilotKitState):
    proverbs: List[str]

async def mock_llm(state: AgentState):
    model = init_chat_model(
        model = "google/gemini-2.5-flash-lite",
        model_provider = "openai",
        base_url="https://ai-gateway.vercel.sh/v1"
    )
    system_message = SystemMessage(content="You are a helpful assistant.")
    # In LangGraph, we typically handle messages differently,
    # but for simple cases we can just pass them to the model.
    # Note: CopilotKitState already includes messages.
    response = await model.ainvoke(
        [
            system_message,
            *state["messages"],
        ]
    )
    return {"messages": response}

graph = StateGraph(AgentState)
graph.add_node("mock_llm", mock_llm)
graph.add_edge(START, "mock_llm")
graph.add_edge("mock_llm", END)
agent = graph.compile(checkpointer=MemorySaver())
