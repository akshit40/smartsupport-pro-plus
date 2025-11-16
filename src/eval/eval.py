# Simple eval harness
from tools.ticket_api import fetch_pending_tickets
from agent_orchestrator import handle_ticket
def run_eval():
    tickets = fetch_pending_tickets()
    for t in tickets:
        handle_ticket(t)
if __name__ == '__main__':
    run_eval()