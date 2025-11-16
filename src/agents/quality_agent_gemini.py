import json
from llm.llm_client import call_llm

QUALITY_SYSTEM = "You are a support quality reviewer. Check the draft for tone, policy violations, factual inaccuracies versus given context, and grammar. Return JSON {issues:[], corrected_draft:'...'}"

def quality_check_with_llm(draft_text, context_snippets):
    prompt = f"Draft:\n{draft_text}\n\nContext:\n{'\n'.join(context_snippets)}\n\nReturn JSON with fields: issues (list) and corrected_draft (string)."
    messages = [{"role":"system","content":QUALITY_SYSTEM}, {"role":"user","content":prompt}]
    raw = call_llm(messages=messages, temperature=0.0)
    try:
        return json.loads(raw)
    except Exception:
        import re
        m = re.search(r"\{.*\}", raw, re.S)
        if m:
            try:
                return json.loads(m.group(0))
            except Exception:
                pass
        return {"issues":["parsing_failed"], "corrected_draft": draft_text}
