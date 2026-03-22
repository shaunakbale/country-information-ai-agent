from langgraph.prebuilt import create_react_agent

from backend.llm.google_gemini_ai import model
from backend.tools.tools import country_information_search_tool
from backend.utils.utils import Utils

utils = Utils()

COUNTRY_INFORMATION_SEARCH_AGENT = create_react_agent(
    name="country_information_search_agent",
    prompt=utils.load_prompt("country_information_search_prompt.txt"),
    model=model,
    tools=[country_information_search_tool]
)

