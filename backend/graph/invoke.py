import asyncio
import uuid

from langchain_core.messages import HumanMessage

from backend.graph.graph import graph

async def invoke_graph(query: str):
    config = {"configurable": {"thread_id": str(uuid.uuid4())}}

    messages = [
        HumanMessage(content=query, name="country_information_search_agent")
    ]

    agent_response = graph.stream(
        {"messages": messages},
        config,
        stream_mode=["messages","updates"]
    )

    for stream_mode, data in agent_response:
        if stream_mode == "messages":
            response, metadata = data
            if isinstance(metadata, dict) and metadata.get("langgraph_node") == "agent":
                text_chunk = (
                    response.content[0]
                    if isinstance(response.content, list)
                       and response.content
                       and isinstance(response.content[0], dict)
                    else response.content
                )
                yield text_chunk

