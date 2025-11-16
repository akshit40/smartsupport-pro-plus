def should_escalate(triage_res: dict, context: list, sentiment: dict) -> bool:
    if triage_res.get('urgency') == 'high':
        return True
    if sentiment.get('sentiment') == 'negative' and triage_res.get('category') in ['billing','returns']:
        return True
    return False
def prepare_escalation_summary(ticket: dict, triage_res: dict, context: list) -> str:
    return f"Escalation for {ticket['id']}: category={triage_res['category']}, reason={ticket['text']}"