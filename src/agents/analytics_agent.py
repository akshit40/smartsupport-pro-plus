# Simple analytics collector
from collections import defaultdict
STORE = defaultdict(int)
def record(event: str):
    STORE[event] += 1
def snapshot():
    return dict(STORE)