from langgraph.graph import END, START, StateGraph
from langchain_core.messages import SystemMessage, BaseMessage
from langchain_openai import ChatOpenAI
from copilotkit import CopilotKitState
from typing import List, Annotated
import os
import operator

class AgentState(CopilotKitState):
    proverbs: List[str]

async def mock_llm(state: AgentState):
    model = ChatOpenAI(model="gpt-4o-mini")
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
agent = graph.compile()
