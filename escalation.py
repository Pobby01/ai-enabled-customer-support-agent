def should_escalate(urgency: str, topic: str) -> bool:
    if urgency == "High":
        return True
    if topic in ["Bug", "Technical Issue"]:
        return True
    return False

def determine_follow_up(escalate: bool) -> str | None:
    if escalate:
        return "Follow up after human agent investigation."
    return None
