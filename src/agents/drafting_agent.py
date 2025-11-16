# Drafting agent uses triage + context to build a draft.
from typing import List, Dict
def generate_draft(ticket: Dict, triage_res: Dict, context: List[Dict]) -> str:
    ctx_text = "\n".join([c["text"] for c in context])
    draft = (
        f"Hi,\n\nThanks for contacting support about: {ticket['text']}\n\n"
        f"Based on our docs:\n{ctx_text}\n\n"
        "Proposed next steps: Please try resetting your password using the link 'Reset Password' or reply with more information.\n\n"
        "Regards,\nSupport Bot"
    )
    return draft