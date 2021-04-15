import fpair
from fpair.pair import _pair


def test_pair():
    assert _pair(1,1) == 4


def test_unpair():
    assert fpair.unpair(4) == (1,1)
