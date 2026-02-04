from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)

RESPONSE_PROMPT = PromptTemplate(
    input_variables=["email", "kb"],
    template="""
You are a professional customer support agent.

Customer email:
{email}

Relevant documentation:
{kb}

Draft a polite, clear, and helpful response.
"""
)

def generate_response(email: str, kb: str) -> str:
    return llm.invoke(RESPONSE_PROMPT.format(email=email, kb=kb)).content
