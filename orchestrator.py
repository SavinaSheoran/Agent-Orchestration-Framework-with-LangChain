from agents.research_agent import create_research_agent
from agents.summarization_agent import create_summarizer_agent

def run_pipeline(query: str):
    research_agent = create_research_agent()
    summarizer_agent = create_summarizer_agent()

    research = research_agent.invoke(
        {"input": f"Research this topic: {query}"},
        config={"configurable": {"session_id": "research"}}
    )

    summary = summarizer_agent.invoke(
        {"input": research.content},
        config={"configurable": {"session_id": "summary"}}
    )

    return {
        "research": research.content,
        "summary": summary.content
    }
