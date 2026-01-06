from langchain_google_genai import ChatGoogleGenerativeAI
import os
GEMINI_KEY = os.getenv("GEMINI_API_KEY")

def email_agent(summary, recipient):
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",api_key=GEMINI_KEY
    )

    prompt = f"""
    Write a professional email to {recipient}
    using the following summary:

    {summary}
    """

    response = llm.invoke(prompt)
    return response.content
