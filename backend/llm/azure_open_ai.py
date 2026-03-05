import os

from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI

load_dotenv()

llm = AzureChatOpenAI(
    azure_deployment="gpt-4o-mini",
    api_version="2024-10-21",
    temperature=0.0
)