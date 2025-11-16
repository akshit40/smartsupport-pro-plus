# Simple quality checks: grammar placeholder and policy check stub
def quality_checks(draft: str):
    issues = []
    if len(draft.split()) < 8:
        issues.append('draft_too_short')
    # policy check stub
    if 'refund' in draft.lower() and 'do not' in draft.lower():
        issues.append('policy_flag')
    return issues