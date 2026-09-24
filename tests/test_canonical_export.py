"""Exported bytes and checkpoint digests depend on content, not field order."""
from aegisrover.storage import checkpoint, jsonl


def test_checkpoint_digest_is_order_independent():
    a = {'b': 1, 'a': {'y': 2, 'x': [3, {'z': 4, 'k': 5}]}, 'c': 'n'}
    b = {'c': 'n', 'a': {'x': [3, {'k': 5, 'z': 4}], 'y': 2}, 'b': 1}

    assert checkpoint.create('n', 1, a)['digest'] == checkpoint.create('n', 1, b)['digest']


def test_checkpoint_verifies_across_field_rewrites():
    c = checkpoint.create('n', 1, {'b': 1, 'a': 2})
    assert checkpoint.verify(c)
    # another client serialised the same state with keys in a different order
    assert checkpoint.verify(dict(c, state={'a': 2, 'b': 1}))
    assert not checkpoint.verify(dict(c, state={'a': 2, 'b': 9}))


def test_jsonl_export_is_order_independent_and_roundtrips():
    rows_a = [{'a': 1, 'b': 2}, {'nested': {'y': 1, 'x': 2}, 'id': 7}]
    rows_b = [{'b': 2, 'a': 1}, {'id': 7, 'nested': {'x': 2, 'y': 1}}]

    assert jsonl.dump(rows_a) == jsonl.dump(rows_b)
    assert jsonl.load(jsonl.dump(rows_a)) == rows_b
