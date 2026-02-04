from graph import build_graph
from schemas import SupportTicketState
from sample_emails import SAMPLE_EMAILS

app = build_graph()

for email in SAMPLE_EMAILS:
    print("\n==============================")
    print("EMAIL:", email)

    state = SupportTicketState(email=email)
    result = app.invoke(state)

    print("\nUrgency:", result.urgency)
    print("Topic:", result.topic)
    print("Escalate:", result.escalate)
    print("Response Draft:\n", result.response_draft)
    print("Follow-up:", result.follow_up)
