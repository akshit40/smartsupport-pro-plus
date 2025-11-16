# Simple memory bank. For production use a vector DB + embeddings.
from collections import defaultdict
class MemoryBank:
    def __init__(self):
        self.store = defaultdict(list)
    def add(self, customer_id: str, note: str):
        self.store[customer_id].append(note)
    def get(self, customer_id: str):
        return self.store.get(customer_id, [])
memory = MemoryBank()