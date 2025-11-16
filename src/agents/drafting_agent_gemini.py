import json
from llm.llm_client import call_llm

DRAFT_SYSTEM = "You are a helpful, concise enterprise support assistant. Use the provided context to draft a customer reply. Always be empathetic, give next steps, and include any policy constraints."

DRAFT_USER_TEMPLATE = """
Ticket: {ticket_text}

Triage: {triage_json}

Context snippets (most relevant first):
{context_snippets}

Write:
- A short empathetic opening
- A clear next-step action
- Any policy notes if relevant
- A closing line

Return: JSON with fields: subject, body, suggested_actions
"""

def generate_draft_with_llm(ticket_text, triage_json, context_snippets):
    prompt = DRAFT_USER_TEMPLATE.format(ticket_text=ticket_text, triage_json=json.dumps(triage_json), context_snippets="\n".join(context_snippets))
    messages = [{"role":"system","content":DRAFT_SYSTEM}, {"role":"user","content":prompt}]
    raw = call_llm(messages=messages, temperature=0.0)
    try:
        return json.loads(raw)
    except Exception:
        import re
        m = re.search(r"\{.*\}", raw, re.S)
        if m:
            try:
                return json.loads(m.group(0))
            except Exception:
                pass
        # fallback: return simple body
        return {"subject":"Response","body":raw, "suggested_actions":[]}
