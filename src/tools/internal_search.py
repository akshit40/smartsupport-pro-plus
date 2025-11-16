# Mock internal search tool. In production replace with a vector DB / ElasticSearch.
from typing import List
KB = [
    {"id": "doc1", "text": "How to reset your password for product X."},
    {"id": "doc2", "text": "Refund policy: refunds processed within 7-10 business days."},
    {"id": "doc3", "text": "Product X compatibility notes and troubleshooting steps."},
]
def search(query: str, k: int = 3) -> List[dict]:
    hits = [d for d in KB if any(tok.lower() in d["text"].lower() for tok in query.split())]
    if not hits:
        hits = KB[:k]
    return hits[:k]
