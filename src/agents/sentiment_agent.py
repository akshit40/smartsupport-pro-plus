# Very small sentiment heuristic for demo
def detect_sentiment(text: str):
    low = text.lower()
    if any(w in low for w in ['angry','upset','furious','not happy','hate']):
        return {'sentiment': 'negative', 'score': 0.2}
    if any(w in low for w in ['thanks','thank','happy']):
        return {'sentiment': 'positive', 'score': 0.9}
    return {'sentiment': 'neutral', 'score': 0.5}