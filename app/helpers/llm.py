from langchain_google_genai import ChatGoogleGenerativeAI
from ..config import LLM_API_KEY
def get_llm():
    llm=ChatGoogleGenerativeAI(
        model = "gemini-flash-latest",
        api_key= LLM_API_KEY
    )
    return llm