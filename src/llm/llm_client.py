"""LLM client wrapper supporting OpenAI and Google Gemini (optional).
- Chooses provider based on LLM_PROVIDER env var: 'openai' or 'gemini'
- Uses OPENAI_API_KEY or GOOGLE_API_KEY from env.
- Returns text or JSON string from model output.
NOTE: This file does not include API keys. Set env vars before running.
"""
import os
import json

LLM_PROVIDER = os.getenv('LLM_PROVIDER', 'openai')  # 'openai' or 'gemini'

def call_llm(messages, model=None, temperature=0.0, max_tokens=800):
    """messages: list of dicts like [{'role':'system','content':'...'}, ...]
    Returns: raw text output (str)
    """
    provider = LLM_PROVIDER.lower()
    if provider == 'openai':
        return _call_openai(messages, model=model or os.getenv('OPENAI_MODEL','gpt-4o-mini'), temperature=temperature, max_tokens=max_tokens)
    elif provider == 'gemini':
        return _call_gemini(messages, model=model or os.getenv('GEMINI_MODEL','gemini-1.5-mini'), temperature=temperature, max_tokens=max_tokens)
    else:
        raise ValueError(f'Unsupported LLM_PROVIDER: {provider}')

def _call_openai(messages, model, temperature, max_tokens):
    try:
        from openai import OpenAI
    except Exception as e:
        raise ImportError('openai package not installed. pip install openai')
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise EnvironmentError('OPENAI_API_KEY not set')
    client = OpenAI(api_key=api_key)
    # Use the Responses API pattern (pseudocode) - adapt to your client version
    # We'll concatenate messages into a single input for simplicity
    prompt = '\n'.join([m.get('content','') for m in messages])
    resp = client.responses.create(model=model, input=prompt, temperature=temperature, max_tokens=max_tokens)
    # Extract text output in a robust way
    out_text = ''
    try:
        # for Responses API
        if hasattr(resp, 'output'):
            # Newer clients wrap outputs differently
            out_parts = []
            for item in resp.output:
                if hasattr(item, 'content'):
                    out_parts.append(getattr(item, 'content'))
                elif isinstance(item, dict) and 'text' in item:
                    out_parts.append(item['text'])
            out_text = '\n'.join(out_parts)
        else:
            out_text = str(resp)
    except Exception:
        out_text = str(resp)
    return out_text

def _call_gemini(messages, model, temperature, max_tokens):
    # Optional Google Gemini client. Install google-generative-ai package to use.
    try:
        import google.generativeai as genai
    except Exception:
        raise ImportError('google.generativeai package not installed. pip install google-generative-ai')
    api_key = os.getenv('GOOGLE_API_KEY')
    if not api_key:
        raise EnvironmentError('GOOGLE_API_KEY not set')
    genai.configure(api_key=api_key)
    prompt = '\n'.join([m.get('content','') for m in messages])
    resp = genai.generate_text(model=model, prompt=prompt, temperature=temperature)
    # resp is usually a dict-like object; extract text
    try:
        return resp.text
    except Exception:
        return str(resp)
