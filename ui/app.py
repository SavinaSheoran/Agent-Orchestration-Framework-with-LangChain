import streamlit as st
import requests

st.title("Agent Orchestration System")

topic = st.text_input("Research Topic")
recipient = st.text_input("Email Recipient")

if st.button("Run Workflow"):
    response = requests.post(
        "http://127.0.0.1:8000/run-workflow",
        json={
            "topic": topic,
            "recipient": recipient
        }
    )

    data = response.json()

    st.subheader("Research")
    st.write(data["research"])

    st.subheader("Summary")
    st.write(data["summary"])

    st.subheader("Email")
    st.write(data["email"])
