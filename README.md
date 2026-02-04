# AI-Powered Customer Support Agent

This project implements an AI-powered customer support agent using
LangChain and LangGraph. The agent automatically processes incoming
support emails, generates responses, and escalates complex issues
to human agents.

## Architecture Overview

The system uses a LangGraph workflow with the following steps:

1. Email ingestion
2. Urgency classification (Low / Medium / High)
3. Topic classification
4. Knowledge base retrieval
5. Response drafting
6. Escalation decision
7. Follow-up scheduling

## Workflow

Email → Classification → Retrieval → Response → Escalation → End

## Technologies

- Python
- LangChain
- LangGraph
- OpenAI GPT Models

## Running the Project

```bash
pip install -r requirements.txt
export OPENAI_API_KEY="your-key"
python app.py


