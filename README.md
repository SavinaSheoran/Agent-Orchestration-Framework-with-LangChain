**Agent-Orchestration-Framework-with-LangChain**

<!-- This project implements a foundational conversational agent using LangChain and Google Gemini LLM.
It fulfills all Week-1 and Week-2 tasks of the assignment, including:

LLM connection

Prompt templates

Chains

Zero-shot agent

Console interface for interaction

Clean OOP (Class-Based) architecture
  -->



## Project Structure

llm_app/
│── .venv/                 # Virtual environment
│── .env                   # API key stored securely
│── .gitignore
│── .python-version
│── main.py                # Main AI agent logic
│── pyproject.toml         # Dependencies + project config
│── README.md              # Project documentation
│── uv.lock




# Installation

# 1. Clone repository

git clone <your-repo-url>
cd llm_app

# 2. Create & activate virtual environment

python -m venv .venv
.venv\Scripts\activate    # Windows

# Environment Variables

GOOGLE_API_KEY=your_api_key_here

# Run the App

python main.py


# Output

You will see:

Explanation of AI

Formatted prompt

Agent-generated response

Interactive console to chat with LLM


# Features

1. Basic Prompt → LLM → Parser Chain

Explains any topic with a simple example.

2. Zero-Shot “Agent-Like” Chain

Works like an intelligent agent with step-by-step reasoning.

3. Interactive Console App

Choose between:

>basic → simple explanation chain

>agent → reasoning agent

>exit → close program