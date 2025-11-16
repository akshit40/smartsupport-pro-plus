# Mock ticket API — simple in-memory tickets
from typing import Dict, List
TICKETS = [
    {"id": "T1", "text": "I can't reset my password, link is not working.", "customer_id": "C1"},
    {"id": "T2", "text": "I want a refund for order #1234, it arrived damaged.", "customer_id": "C2"},
    {"id": "T3", "text": "My device X overheats after 10 minutes of use.", "customer_id": "C3"},
]
def fetch_pending_tickets() -> List[Dict]:
    return TICKETS
def post_draft_response(ticket_id: str, draft: str) -> None:
    print(f"[TicketAPI] Draft posted for {ticket_id}:\n{draft}\n")