import bpair


def test_pair():
    assert bpair.pair(4,5) == 0


def test_unpair():
    assert bpair.unpair(5) == 0
