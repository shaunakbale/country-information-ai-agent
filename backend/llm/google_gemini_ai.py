import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

model = ChatGoogleGenerativeAI(
    model=os.getenv("GOOGLE_GEMINI_MODEL"),
    temperature=0.0,
    api_key=os.getenv("GOOGLE_GEMINI_KEY")
)