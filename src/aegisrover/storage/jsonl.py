import json

from .repository import canonical_json


def dump(rows):
    return ''.join((canonical_json(r) + '\n' for r in rows))


def load(text):
    return [json.loads(x) for x in text.splitlines() if x.strip()]
