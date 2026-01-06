**Agent-Orchestration-Framework-with-LangChain**

## Project Overview
```
This project implements a multi-agent orchestration framework using LangChain and Google Gemini LLMs.
The system demonstrates how intelligent agents can collaborate, manage memory, invoke tools, and automate complex workflows through structured orchestration.

The project progresses incrementally across four milestones, starting from a basic conversational agent and evolving into a full workflow automation system with API and UI exposure.
```

## Folder Structure

```
INTERNSHIP_PROJECT/
├── agents/
│   ├── email_agent.py
│   ├── research_agent.py
│   └── summarization_agent.py
│
├── ui/
│   └── app.py
│
├── .env
├── .gitignore
│
├── agent.py
├── agent_memory.py
├── Agile_Document.xlsx
├── LICENSE
├── main.py
├── memory.json
├── memory.py
├── orchestrator.py
├── prompts.py
├── pyproject.toml
├── README.md
├── tools.py
├── uv.lock
└── workflow.py

```

## Requirements
```
Python 3.9+

LangChain

Google Generative AI (Gemini)

Requests

python-dotenv

```

## Milestone 1: Environment Setup & Basic Agent Creation

## Objective
```
Build a foundational conversational agent using LangChain and a real LLM.
```
## Key Features Implemented
```
- Python + LangChain development environment

- Integration with Google Gemini LLM

- Exploration of LangChain core components:
    >LLMs
    >Prompts
    >Agents

Prompt-based agent behavior using a system prompt

Console-based interactive interface
```

## Evidence in Code
```
ChatGoogleGenerativeAI used in agent.py and main.py

System prompt defined in prompts.py

Agent created using create_agent

Interactive loop implemented in main.py
```
## Output
```
Functional conversational AI agent

User can chat with the agent via terminal
```
## Milestone 2: Tool Integration & API Calling

## Objective
```
Extend the agent’s capabilities using LangChain tools and external APIs.
```
## Tools Implemented
```
1️. Calculator Tool

Performs arithmetic calculations

Automatically invoked for math-related queries

2️. Stock Price Tool

Fetches real-time stock data using Alpha Vantage API

Demonstrates real API integration
```
## Additional Features
```
>Tool abstraction using @tool
>Prompt rules guiding correct tool usage
>Error handling for API failures
>Agent automatically decides when to use tools
```
## Evidence in Code
```
Tools defined in tools.py

Tools passed into agent context

Prompt rules instructing tool usage

Tool invocation tested via console
```
## Output
```
Agent responds intelligently using tools

Successful demonstration of agent-tool interaction
```

## Milestone 3: Multi-Agent Orchestration & Memory Management 
## Objective
```
Enable agent collaboration with memory-based reasoning.
```

## Key Features Implementd
```
- Multiple agent roles defined:
    > Research Agent
    > Summarization Agent

- Orchestration pipeline to control agent collaboration

- Shared semantic memory using FAISS vector store

- Embedding-based memory storage and retrieval

- Agent outputs influencing subsequent agent decisions
```

## Evidence in code
```
- Research and Summarization agents defined in agents/ directory

- Orchestration logic implemented in orchestrator.py

- Shared memory implemented in shared_memory.py

- FAISS vector store with GoogleGenerativeAIEmbeddings

- Multi-agent execution triggered from main.py
```

## Output
```
- Research and Summarization agents defined in agents/ directory

- Orchestration logic implemented in orchestrator.py

- Shared memory implemented in shared_memory.py

- FAISS vector store with GoogleGenerativeAIEmbeddings

- Multi-agent execution triggered from main.py
```

## Milestone 4: Workflow Automation, API & UI

## Objective
```
Automate a complete multi-step workflow using multiple agents, 
exposed through a REST API and an interactive UI.
```

## Workflow Implemented
```
1️. Research Phase
   - Research Agent gathers relevant information for the given topic
2️. Summarization Phase
   - Summarization Agent condenses research output into a structured summary
3️. Email Composition Phase
   - Email Agent generates a professional email based on the summary
```

## Additional Features
```
>Multi-step workflow orchestration logic

>Clear separation of agent responsibilities

>REST API implementation using FastAPI

>Interactive frontend using Streamlit

>End-to-end automation triggered by a single user input
```

## Evidence in Code
```
Full workflow logic implemented in workflow.py

Agent coordination handled by orchestrator.py

REST API exposed via ui/app.py

Individual agent logic inside agents/ directory
```

## Output
```
User provides a topic or instruction via UI or API

System automatically executes research → summarize → email workflow

Final composed output returned to the user through UI/API
```

##  How to Run the Project
```
1️⃣ Install Dependencies
pip install -r requirements.txt

2️⃣ Set Environment Variables

Create a .env file:

API_KEY=your_llm_api_key

3️⃣ Run Console Mode
python main.py

4️⃣ Run Workflow API
python -m uvicorn ui.app:app --reload
PS C:\Users\Lenovo\Downloads\internship_Project> cd ui
PS C:\Users\Lenovo\Downloads\internship_Project\ui> python -m streamlit run app.py

5️⃣ Access API Docs
http://127.0.0.1:8000/docs

```

## Conclusion
```
This project successfully meets and exceeds the requirements for:

• Milestone 1: Basic Agent Creation
• Milestone 2: Tool Integration & API Calling
• Milestone 3: Multi-Agent Orchestration & Memory
• Milestone 4: Workflow Automation, API & UI

It demonstrates strong proficiency in LangChain fundamentals,
agent-based system design, tool orchestration, memory management,
and real-world AI workflow automation.
```


## ## Deployed Link

```
Local Deployment (Run Locally)
FastAPI Docs: http://127.0.0.1:8000/docs
Streamlit UI: http://localhost:8501

```
