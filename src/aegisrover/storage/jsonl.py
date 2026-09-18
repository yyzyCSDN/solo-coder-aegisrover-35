import json

def dump(rows):
    return ''.join((json.dumps(r) + '\n' for r in rows))

def load(text):
    return [json.loads(x) for x in text.splitlines() if x.strip()]
