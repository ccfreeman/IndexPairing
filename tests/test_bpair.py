import bpair
import numpy as np


def test_pair():
    a = np.array([1, 3], dtype=np.uint32)
    b = np.array([15, 7], dtype=np.uint32)
    arr = np.array([[x1, x2] for x1, x2 in zip(a, b)])
    actual = bpair.pair(arr)
    expected = np.array([4294967311, 12884901895], dtype=np.uint64)
    assert all([x == y for x, y in zip(actual, expected)])


def test_unpair():
    expected_a = np.array([1, 3], dtype=np.uint32)
    expected_b = np.array([15, 7], dtype=np.uint32)
    actual_a, actual_b = bpair.unpair(np.array([4294967311, 12884901895], dtype=np.uint64))
    assert all([x == y for x,y in zip(actual_a, expected_a)]) and all([x == y for x,y in zip(actual_b, expected_b)])
