# main.py 

import os
from dotenv import load_dotenv

# LangChain 
from langchain_google_genai import ChatGoogleGenerativeAI

# Local modules
from agent import run_agent
from memory import Memory

load_dotenv()

GEMINI_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_KEY:
    raise ValueError("GEMINI_API_KEY missing in .env file")

# Basic Gemini LLM fun test

def fun_test():
    print("\n--- Gemini LLM fun Test ---")
    # create a short-lived LLM instance for a quick check
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        google_api_key=GEMINI_KEY,
        temperature=0.2
    )

    try:
        # .invoke returns a response-like object in the wrappers used earlier
        resp = llm.invoke("Explain artificial intelligence in one simple sentence.")
        # The wrapper sometimes returns an object with `.content` or simple str; handle both
        out = getattr(resp, "content", None) or str(resp)
        print("Gemini test output:", out)
    except Exception as e:
        print("Gemini fun test failed:", str(e))
    print("--- end fun test ---\n")


# Console agent runner

def run_console_agent():
    # initialize persistent JSON memory
    mem = Memory(memory_file="memory.json")

    # build the agent runnable (from agent.py)

    print("\n-- Gemini Tool-Augmented Agent (Milestone 1 & 2) --")
    print("Type 'exit' to quit, 'memory show' to see saved memory, 'memory clear' to clear memory.\n")

    session_id = "default"  # optional session identifier if you extend memory logic

    while True:
        user_input = input("You: ").strip()
        if not user_input:
            continue

        if user_input.lower() == "exit":
            print("Goodbye!!!")
            break

        # memory utilities
        if user_input.lower() == "memory show":
            print("Stored memory:", mem.data)
            continue
        if user_input.lower() == "memory clear":
            mem.clear()
            print("Memory cleared.")
            continue
        result = run_agent(user_input)


        # Save last user message to memory 
        try:
            mem.add("last_user_input", user_input)
        except Exception:
            # don't stop on memory errors
            pass
 
        print("AI:", result, "\n")

        # Save last AI response into memory
        try:
            mem.add("last_ai_response", result)
        except Exception:
            pass



if __name__ == "__main__":
    print("\nStarting main.py (Gemini edition)\n")
    # fun_test()
    run_console_agent()




