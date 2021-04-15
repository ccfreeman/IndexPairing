import fpair
from fpair.pair import _pair, _unpair


def test_pair():
    assert _pair(1,1) == 4


def test_unpair():
    assert _unpair(4) == [1,1]
