# LLM-capable agent imports (Gemini/OpenAI wrappers)
import os
LLM_PROVIDER = os.getenv('LLM_PROVIDER', None)
try:
    if LLM_PROVIDER:
        from agents.triage_agent_gemini import triage_with_llm as triage_llm
        from agents.drafting_agent_gemini import generate_draft_with_llm as generate_draft_llm
        from agents.quality_agent_gemini import quality_check_with_llm as quality_check_llm
    else:
        triage_llm = None
        generate_draft_llm = None
        quality_check_llm = None
except Exception:
    triage_llm = None
    generate_draft_llm = None
    quality_check_llm = None

import argparse
from tools.ticket_api import fetch_pending_tickets, post_draft_response
from agents.triage_agent import triage
from agents.knowledge_agent import fetch_context
from agents.drafting_agent import generate_draft
from agents.quality_agent import quality_checks
from agents.sentiment_agent import detect_sentiment
from agents.escalation_agent import should_escalate, prepare_escalation_summary
from agents.loop_agent import schedule_follow_up
from agents.analytics_agent import record, snapshot
from memory.memory_bank import memory
from utils.logging import log_event

def handle_ticket(ticket):
    log_event('ticket_received', {'ticket_id': ticket['id']})
    triage_res = (triage_llm(ticket['text']) if triage_llm else triage(ticket['text']))
    log_event('triage_done', {'ticket_id': ticket['id'], 'triage': triage_res})
    context = fetch_context(ticket['text'])
    log_event('context_fetched', {'ticket_id': ticket['id'], 'context_ids': [c['id'] for c in context]})
    sentiment = detect_sentiment(ticket['text'])
    log_event('sentiment', {'ticket_id': ticket['id'], 'sentiment': sentiment})
    if generate_draft_llm:
        # Use RAG LLM draft (returns JSON or dict)
        snippets = [c['text'] for c in context]
        draft_obj = generate_draft_llm(ticket['text'], triage_res, snippets)
        if isinstance(draft_obj, dict):
            draft = draft_obj.get('body', str(draft_obj))
        else:
            draft = str(draft_obj)
    else:
        draft = generate_draft(ticket, triage_res, context)
    log_event('draft_generated', {'ticket_id': ticket['id']})
    issues = quality_checks(draft)
    log_event('quality_checks', {'ticket_id': ticket['id'], 'issues': issues})
    if issues:
        # naive repair: append apology
        draft += "\n\nNote: We apologize for the inconvenience. We'll follow up." 
    post_draft_response(ticket['id'], draft)
    record('drafts_posted')
    if should_escalate(triage_res, context, sentiment):
        summary = prepare_escalation_summary(ticket, triage_res, context)
        log_event('escalation_created', {'ticket_id': ticket['id'], 'summary': summary})
        record('escalations')
    memory.add(ticket['customer_id'], f"last_ticket:{ticket['id']}")
    follow = schedule_follow_up(ticket['id'], {'state':'demo'})
    log_event('follow_up', follow)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--demo', action='store_true')
    args = parser.parse_args()
    tickets = fetch_pending_tickets()
    for t in tickets:
        handle_ticket(t)
    print('Demo finished')
