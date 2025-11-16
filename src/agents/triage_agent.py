# Mock triage agent
from typing import Dict
CATEGORY_KEYWORDS = {
    "password": "auth",
    "refund": "billing",
    "damaged": "returns",
    "overheat": "hardware",
}
def triage(ticket_text: str) -> Dict:
    text = ticket_text.lower()
    for k, cat in CATEGORY_KEYWORDS.items():
        if k in text:
            return {"category": cat, "urgency": "high" if "not" in text or "can't" in text or "urgent" in text else "medium"}
    # small sentiment heuristic
    if any(w in text for w in ['angry','upset','frustrat']):
        return {"category": "general", "urgency": "high"}
    return {"category": "general", "urgency": "low"}