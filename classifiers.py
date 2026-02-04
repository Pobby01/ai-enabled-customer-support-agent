from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

URGENCY_PROMPT = PromptTemplate(
    input_variables=["email"],
    template="""
Classify the urgency of this customer support email.
Return only one word: Low, Medium, or High.

Email:
{email}
"""
)

TOPIC_PROMPT = PromptTemplate(
    input_variables=["email"],
    template="""
Classify the topic of this customer support email.
Choose one:
Account, Billing, Bug, Feature Request, Technical Issue

Email:
{email}
"""
)

def classify_urgency(email: str) -> str:
    return llm.invoke(URGENCY_PROMPT.format(email=email)).content.strip()

def classify_topic(email: str) -> str:
    return llm.invoke(TOPIC_PROMPT.format(email=email)).content.strip()
