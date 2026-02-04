from pydantic import BaseModel
from typing import Optional, List

class SupportTicketState(BaseModel):
    email: str
    urgency: Optional[str] = None
    topic: Optional[str] = None
    kb_result: Optional[str] = None
    response_draft: Optional[str] = None
    escalate: Optional[bool] = False
    follow_up: Optional[str] = None
