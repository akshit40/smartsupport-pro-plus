from tools.internal_search import search
def fetch_context(ticket_text: str):
    hits = search(ticket_text, k=3)
    return hits