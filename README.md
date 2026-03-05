# Country Information AI Agent

A conversational AI chatbot that answers questions about any country using real-time data from the [RestCountries API](https://restcountries.com). Built with LangGraph, Google Gemini, and Streamlit.

Deployed Link: https://country-information-ai-agent.streamlit.app

## Features

- **Natural Language Q&A** - Ask questions like "What is the capital of Japan?" or "Tell me about Brazil" and get clear, human-friendly answers.
- **Real-Time Country Data** - Fetches live information (capital, population, languages, currency, region, etc.) from the RestCountries API. No stale or hallucinated data.
- **ReAct Agent with Tool Use** - Uses a LangGraph ReAct agent that decides when to call the country search tool and how to interpret the results.
- **Streaming Responses** - Answers are streamed token-by-token to the UI for a responsive chat experience.
- **Chat History** - The Streamlit UI maintains conversation history within a session so you can ask follow-up questions.
- **Configurable LLM Backend** - Ships with Google Gemini (active) and Azure OpenAI (available), switchable by changing a single import.

## Prerequisites

- Python 3.10+
- A Google Gemini API key (or Azure OpenAI credentials)

## Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/shaunakbale/country-information-ai-agent
cd cloudeagle-assignment
```

### 2. Create a `.env` file

```env
GOOGLE_GEMINI_KEY=your-google-gemini-api-key
GOOGLE_GEMINI_MODEL=gemini-flash-lite-latest

# Optional: LangSmith tracing
LANGSMITH_TRACING=true
LANGSMITH_ENDPOINT=https://api.smith.langchain.com
LANGSMITH_API_KEY=your-langsmith-api-key
LANGSMITH_PROJECT=cloudeagle-assignment
```

### 3. Install dependencies

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 4. Run the app

```bash
streamlit run frontend/app.py
```

The app opens at **http://localhost:8501**.

## Run with Docker

```bash
docker build -t cloudeagle-assignment .
docker run -env-file .env -p 8501:8501 cloudeagle-assignment
```

## Example Questions

| Question | What you get |
|---|---|
| What is the capital of France? | The capital of France is Paris.|
| Tell me about the currencies used in Japan | Japanese Yen (JPY) |
| What languages are spoken in Switzerland? | German, French, Italian, Romansh |
| What region is Nigeria in? | Africa, Western Africa |
