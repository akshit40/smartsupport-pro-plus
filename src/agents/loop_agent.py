# Loop agent schedules follow-ups (demo: immediate simulation)
def schedule_follow_up(ticket_id: str, state: dict):
    # In production integrate with scheduler; here we simulate an immediate check
    return {'ticket_id': ticket_id, 'action': 'follow_up_scheduled'}