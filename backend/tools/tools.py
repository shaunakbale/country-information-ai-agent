import requests
from langchain_core.tools import tool


@tool(
    name_or_callable="country_information_search",
    description="Search country information using an open source API"
)
def country_information_search_tool(country_name: str) -> list:
    """
    Search country information using the RestCountries API
    """

    try:
        url = f"https://restcountries.com/v3.1/name/{country_name}"
        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            return []

        country_information = response.json()

        if not country_information:
            return []

        return country_information

    except Exception:
        return []