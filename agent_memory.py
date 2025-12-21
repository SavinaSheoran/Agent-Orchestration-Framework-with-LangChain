from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

def create_memory():
    """
    Returns a factory-compatible memory handler.
    This replaces ConversationBufferMemory.
    """
    return InMemoryChatMessageHistory()
