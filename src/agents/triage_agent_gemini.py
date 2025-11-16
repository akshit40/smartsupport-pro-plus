import json
from llm.llm_client import call_llm

TRIAGE_SYSTEM = """You are an enterprise support classifier. Extract: category, subcategory, intent, and urgency.\nReturn JSON only with fields: category, subcategory, intent, urgency (low|medium|high)."""

TRIAGE_FEWSHOT = [
    {"role":"user","content":"Ticket: 'I can't reset my password, link not working.'"},
    {"role":"assistant","content":'{"category":"auth","subcategory":"password_reset","intent":"reset_request","urgency":"high"}'},
    {"role":"user","content":"Ticket: 'My order arrived damaged, I want a refund.'"},
    {"role":"assistant","content":'{"category":"billing","subcategory":"refund","intent":"refund_request","urgency":"high"}'}
]

def triage_with_llm(ticket_text: str) -> dict:
    messages = [{"role":"system","content":TRIAGE_SYSTEM}]
    messages += TRIAGE_FEWSHOT
    messages.append({"role":"user","content":f"Ticket: '{ticket_text}'\n\nReturn JSON only."})
    raw = call_llm(messages=messages, temperature=0.0)
    # attempt to extract JSON from raw
    try:
        j = json.loads(raw)
        return j
    except Exception:
        # try to find JSON substring
        import re
        m = re.search(r"\{.*\}", raw, re.S)
        if m:
            try:
                return json.loads(m.group(0))
            except Exception:
                pass
        # fallback to simple heuristic
        return {"category":"general","subcategory":"unknown","intent":"unknown","urgency":"low"}
