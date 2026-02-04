from langgraph.graph import StateGraph, END
from schemas import SupportTicketState
from classifiers import classify_urgency, classify_topic
from retriever import search_knowledge_base
from responder import generate_response
from escalation import should_escalate, determine_follow_up

def urgency_node(state: SupportTicketState):
    state.urgency = classify_urgency(state.email)
    return state

def topic_node(state: SupportTicketState):
    state.topic = classify_topic(state.email)
    return state

def retrieval_node(state: SupportTicketState):
    state.kb_result = search_knowledge_base(state.topic)
    return state

def response_node(state: SupportTicketState):
    state.response_draft = generate_response(state.email, state.kb_result)
    return state

def escalation_node(state: SupportTicketState):
    state.escalate = should_escalate(state.urgency, state.topic)
    state.follow_up = determine_follow_up(state.escalate)
    return state

def build_graph():
    graph = StateGraph(SupportTicketState)

    graph.add_node("urgency", urgency_node)
    graph.add_node("topic", topic_node)
    graph.add_node("retrieve", retrieval_node)
    graph.add_node("respond", response_node)
    graph.add_node("escalate", escalation_node)

    graph.set_entry_point("urgency")
    graph.add_edge("urgency", "topic")
    graph.add_edge("topic", "retrieve")
    graph.add_edge("retrieve", "respond")
    graph.add_edge("respond", "escalate")
    graph.add_edge("escalate", END)

    return graph.compile()
