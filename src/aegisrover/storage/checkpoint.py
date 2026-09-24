import hashlib

from .repository import canonical_json


def _digest(state):
    return hashlib.sha256(canonical_json(state).encode()).hexdigest()


def create(name, sequence, state):
    return {'name': name, 'sequence': sequence, 'state': state, 'digest': _digest(state)}


def verify(c):
    return c['digest'] == _digest(c['state'])
