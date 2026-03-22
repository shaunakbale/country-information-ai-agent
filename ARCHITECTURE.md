# Architecture Overview

## High-Level Flow

1. **User** sends a question via the Streamlit chat UI (`frontend/app.py`).
2. **LangGraph StateGraph** (`backend/graph/graph.py`) receives the message and routes it to the agent.
3. **ReAct Agent** (`backend/agents/country_information_agent.py`) decides whether to call the country search tool or respond directly.
4. **Country Search Tool** (`backend/tools/tools.py`) fetches live data from the RestCountries API and returns it as JSON.
5. The agent interprets the JSON and streams a natural-language answer back to the UI.

## Project Structure

- `frontend/app.py` - Streamlit chat interface
- `backend/agents/country_information_agent.py` - ReAct agent definition
- `backend/graph/state.py` - Graph state schema (message list)
- `backend/graph/graph.py` - StateGraph wiring: START -> agent -> END
- `backend/graph/invoke.py` - Streams graph output back to the UI
- `backend/llm/google_gemini_ai.py` - Google Gemini model config (active)
- `backend/llm/azure_open_ai.py` - Azure OpenAI model config (alternative)
- `backend/prompts/country_information_search_prompt.txt` - System prompt
- `backend/tools/tools.py` - RestCountries API tool
- `backend/utils/utils.py` - Prompt file loader
- `requirements.txt` - Python dependencies
- `Dockerfile` - Container setup
- `.env` - API keys (not committed)

## Component Details

### Frontend - Streamlit
Stores messages in `st.session_state`, renders them on each rerun, and uses `st.write_stream()` to display the agent's streamed response token-by-token.

### Graph - LangGraph
A single-node `StateGraph` (START -> agent -> END). State is a `TypedDict` with a `messages` field managed by LangGraph's `add_messages` reducer. `MemorySaver` checkpointer enables conversation memory per thread.

### Agent - ReAct
Built with `langgraph.prebuilt.create_react_agent`. Receives the user's question plus a system prompt, decides whether to call the tool, and produces a natural-language answer from the tool's JSON response. The system prompt constrains the agent to only use tool-returned data.

### Tool - RestCountries API
A `@tool`-decorated function that takes a `country_name`, calls `https://restcountries.com/v3.1/name/{country_name}`, and returns the JSON response (capital, population, languages, currencies, region, etc.).

### LLM
Two model configurations available:

| Provider | File | Model |
|---|---|---|
| Google Gemini | `google_gemini_ai.py` | `gemini-flash-lite-latest` |
| Azure OpenAI | `azure_open_ai.py` | `gpt-4o-mini` |

Currently using Google Gemini, set by the import in `country_information_agent.py`.

### Tracing - LangSmith
LangSmith is used for tracing and observability. When enabled via environment variables (`LANGSMITH_TRACING`, `LANGSMITH_API_KEY`, `LANGSMITH_ENDPOINT`, `LANGSMITH_PROJECT`), all agent runs, tool calls, and LLM interactions are logged to LangSmith for debugging and monitoring.
