from knowledge_base import KNOWLEDGE_BASE

def search_knowledge_base(topic: str) -> str:
    return KNOWLEDGE_BASE.get(topic, "No relevant documentation found.")
