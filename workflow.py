from orchestrator import run_pipeline
from agents.email_agent import email_agent

def run_full_workflow(topic, recipient):
    result = run_pipeline(topic)

    email = email_agent(
        summary=result["summary"],
        recipient=recipient
    )

    return {
        "research": result["research"],
        "summary": result["summary"],
        "email": email
    }
