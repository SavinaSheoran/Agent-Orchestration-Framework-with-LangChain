**Agent-Orchestration-Framework-with-LangChain**

## Project Overview
```
-- The agent can:

Engage in natural language conversation

Perform arithmetic calculations using a Calculator tool

Fetch real-time stock price information using an external API

Handle tool errors gracefully

Maintain basic persistent memory across interactions

The project runs entirely in the terminal/console and is designed for learning and demonstration purposes.
```

## Folder Structure

```
llm_app/
│
├── main.py # Console runner
├── agent.py # Agent creation & execution logic
├── tools.py # Custom tools (Calculator, Stock Price)
├── memory.py # Persistent JSON memory handler
├── prompts.py # System prompt for the agent
├── memory.json # Auto-generated memory store
├── .env # Environment variables (API keys)
└── README.md # Project documentation
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

## How to Run the Project
```
python main.py
```

## Console Commands
```
exit → Quit the application

memory show → View stored memory

memory clear → Clear memory
```

## Conclusion
```
This project successfully meets and exceeds the requirements for:

-- Milestone 1: Basic Agent Creation

-- Milestone 2: Tool Integration & API Calling

It demonstrates a strong understanding of LangChain fundamentals, agent orchestration, prompt engineering, and practical tool usage with real APIs.
```