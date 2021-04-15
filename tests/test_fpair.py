import fpair


def test_pair():
    assert fpair.pair(1,1) == 4


def test_unpair():
    assert fpair.unpair(4) == (1,1)
