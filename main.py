# # main.py

# import os
# import sys
from dotenv import load_dotenv


# # LangChain
#from langchain_google_genai import ChatGoogleGenerativeAI

# # Milestone 1 & 2
# from agent import run_agent
# from memory import Memory

# # Milestone 3
# from orchestrator import run_pipeline

load_dotenv()

# GEMINI_KEY = os.getenv("GEMINI_API_KEY")
# if not GEMINI_KEY:
#     raise ValueError("GEMINI_API_KEY missing in .env file")


# # Optional: Gemini sanity test

# def fun_test():
#     print("\n--- Gemini LLM fun Test ---")
#     llm = ChatGoogleGenerativeAI(
#         model="gemini-2.0-flash",
#         google_api_key=GEMINI_KEY,
#         temperature=0.2
#     )

#     resp = llm.invoke("Explain artificial intelligence in one simple sentence.")
#     print("Gemini test output:", getattr(resp, "content", resp))
#     print("--- end fun test ---\n")


# # Milestone 1 & 2: Single-Agent Console

# def run_single_agent_console():
#     mem = Memory(memory_file="memory.json")

#     print("\n-- Gemini Tool-Augmented Agent (Milestone 1 & 2) --")
#     print("Type 'exit' to quit, 'memory show', 'memory clear'\n")

#     while True:
#         user_input = input("You: ").strip()

#         if user_input.lower() == "exit":
#             print("Goodbye!")
#             break

#         if user_input.lower() == "memory show":
#             print("Stored memory:", mem.data)
#             continue

#         if user_input.lower() == "memory clear":
#             mem.clear()
#             print("Memory cleared.")
#             continue

#         result = run_agent(user_input)

#         mem.add("last_user_input", user_input)
#         mem.add("last_ai_response", result)

#         print("AI:", result, "\n")


# # Milestone 3: Multi-Agent Orchestration

# def run_multi_agent_console():
#     print("\n-- Multi-Agent Orchestration (Milestone 3) --")
#     print("Research Agent → Shared Memory → Summarization Agent\n")
#     print("Type 'exit' to quit\n")

#     while True:
#         query = input("Research Topic: ").strip()

#         if query.lower() == "exit":
#             print("Goodbye!")
#             break

#         result = run_pipeline(query)

#         print("\n--- Research Output ---")
#         print(result["research"])

#         print("\n--- Summary Output ---")
#         print(result["summary"])
#         print("\n" + "-" * 60 + "\n")


# # Application Entry Point

# def main():
#     print("\nStarting Gemini Agent Framework\n")
#     print("Choose Mode:")
#     print("1 → Milestone 1 & 2 (Single Agent + Tools)")
#     print("2 → Milestone 3 (Multi-Agent Orchestration)\n")

#     choice = input("Enter choice (1 or 2): ").strip()

#     if choice == "1":
#         run_single_agent_console()
#     elif choice == "2":
#         run_multi_agent_console()
#     else:
#         print("Invalid choice. Restart application.")


# if __name__ == "__main__":
#     main()

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from workflow import run_full_workflow

app = FastAPI(title="Multi-Agent Workflow API")

class TopicRequest(BaseModel):
    topic: str
    recipient: str

@app.post("/run-workflow")
def run_workflow(request: TopicRequest):
    return run_full_workflow(request.topic, request.recipient)

@app.get("/")
def root():
    return {"message": "API is running"}

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
