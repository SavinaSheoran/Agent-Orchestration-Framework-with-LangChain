from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
import os
from dotenv import load_dotenv

load_dotenv()



#  Class: LLMAgentApp
class LLMApp:

    def __init__(self):
        self._check_api_key()
        self.llm = self._connect_llm()
        
        # initialize chains
        self.basic_chain = self._create_basic_chain()
        self.agent_chain = self._create_agent_chain()

    # Check API Key
    def _check_api_key(self):
        if not os.getenv("GOOGLE_API_KEY"):
            raise ValueError("GOOGLE_API_KEY missing in .env file")
        print("API Key Loaded Successfully!")

    # Connect to Gemini using LangChain
    def _connect_llm(self):
        print("Connecting to Gemini LLM...")
        llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            temperature=0.3
        )
        print("Gemini LLM connected!\n")
        return llm

    
    # Create Basic Prompt → LLM → Parser Chain
    
    def _create_basic_chain(self):
        prompt = PromptTemplate(
            input_variables=["topic"],
            template="Explain {topic} with a simple example."
        )
        chain = prompt | self.llm | StrOutputParser()
        self.basic_prompt = prompt   # save for testing
        return chain

    
    # Create Zero-Shot Agent-Like Chain
    
    def _create_agent_chain(self):
        agent_prompt = PromptTemplate(
            input_variables=["task"],
            template=(
                "Act as an intelligent agent. Solve the task step-by-step.\n"
                "Task: {task}\n"
                "Answer:"
            )
        )
        chain = agent_prompt | self.llm | StrOutputParser()
        self.agent_prompt = agent_prompt
        return chain

    
    # Test LLM
    
    def test_llm(self):
        response = self.llm.invoke("Explain AI in simple words.")
        print("LLM Test Response:", response.content)

    
    # Test Prompt Formatting
    
    def test_prompt_format(self):
        print("\nFORMATTED PROMPT:")
        print(self.basic_prompt.format(topic="Machine Learning"))

    
    # Test Full Runnable Sequence
    
    def test_chain(self):
        print("\nTesting Basic Chain with RunnableSequence...")
        chain = RunnableSequence(self.basic_prompt | self.llm | StrOutputParser())
        output = chain.invoke({"topic": "Neural Networks"})
        print("CHAIN OUTPUT:", output)

   
    # Console Chat Interface
    
    def run_console(self):
        print("\n=== LangChain Console Agent ===")
        print("Type 'basic' to use simple chain")
        print("Type 'agent' to use reasoning agent")
        print("Type 'exit' to quit\n")

        while True:
            mode = input("Select mode (basic/agent/exit): ").lower()

            if mode == "exit":
                print("Goodbye!")
                break

            if mode not in ["basic", "agent"]:
                print("Invalid mode. Try again.\n")
                continue

            user_input = input("\nYou: ")

            if mode == "basic":
                response = self.basic_chain.invoke({"topic": user_input})
            else:
                response = self.agent_chain.invoke({"task": user_input})

            print("AI:", response, "\n")



#  MAIN EXECUTION

if __name__ == "__main__":
    app = LLMApp()


    app.test_llm()
    app.test_prompt_format()
    app.test_chain()

    # run console
    app.run_console()
