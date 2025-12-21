# agent.py  
import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.agents import create_agent
from tools import tools
from prompts import system_prompt as  SYSTEM_PROMPT

load_dotenv()



# BUILD THE AGENT 

def run_agent(user_input):
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.3,

    )
    

    agent = create_agent(
        llm,
        tools=tools,
        system_prompt = """
        You are a smart agent with access to tools.

        Rules:
        1. Use the CALCULATOR tool for any math request.
        2. Use stock_price tool for stock price information for a company.
        3. If the user asks mixed questions (math + stock price), handle both.
        4. If a tool returns an error, apologize and offer other help.
        5. If no tool is needed, answer normally.
        6. Always explain final answers clearly.
        """
    )

    result = agent.invoke(
        {"messages": [{"role": "user", "content": user_input}]},)
    return result['messages'][-1].content
