from dotenv import load_dotenv
from langchain_core.messages import AIMessage
from langgraph.checkpoint.base import BaseCheckpointSaver
from langgraph.checkpoint.memory import MemorySaver
from langgraph.constants import START, END
from langgraph.graph import StateGraph

from backend.agents.country_information_agent import COUNTRY_INFORMATION_SEARCH_AGENT
from backend.graph.state import State

load_dotenv()

def country_information_search_agent_node(state: State):
    response = COUNTRY_INFORMATION_SEARCH_AGENT.invoke(
        state
    )
    return {
        "messages": state["messages"] + [
            AIMessage(content=response["messages"][-1].content)
        ]
    }

checkpointer = MemorySaver()

graph_builder = StateGraph(State)

graph_builder.add_node(
    "country_information_search_agent",
    country_information_search_agent_node
)

graph_builder.add_edge(START, "country_information_search_agent")
graph_builder.add_edge("country_information_search_agent", END)

graph = graph_builder.compile(checkpointer=checkpointer)