import json, time
def log_event(event_type: str, payload: dict):
    print(json.dumps({"ts": time.time(), "type": event_type, "payload": payload}))