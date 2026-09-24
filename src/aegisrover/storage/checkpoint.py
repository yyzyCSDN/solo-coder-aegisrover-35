import hashlib

from .repository import canonical_json

def create(name, sequence, state):
    body = canonical_json(state).encode()
    return {'name': name, 'sequence': sequence, 'state': state, 'digest': hashlib.sha256(body).hexdigest()}

def verify(c):
    return c['digest'] == hashlib.sha256(canonical_json(c['state']).encode()).hexdigest()
