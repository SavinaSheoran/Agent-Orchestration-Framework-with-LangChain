from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory

# individual memory store
import os
_store = {}
GEMINI_KEY = os.getenv("GEMINI_API_KEY")


def _get_memory(session_id: str):
    if session_id not in _store:
        _store[session_id] = InMemoryChatMessageHistory()
    return _store[session_id]

def create_research_agent():
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",api_key=GEMINI_KEY
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a Research Agent. Provide key factual points."),
        ("human", "{input}")
    ])

    chain = prompt | llm

    return RunnableWithMessageHistory(
        chain,
        _get_memory,
        input_messages_key="input",
        history_messages_key="history"
    )
