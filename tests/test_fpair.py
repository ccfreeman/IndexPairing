import fpair
from fpair.pair import _pair, _unpair
import numpy as np

def test_pair():
    assert _pair(1,1) == 4


def test_unpair():
    assert _unpair(4) == [1,1]

import numpy as np


def test_pair_arr():
    a = np.array([1, 3], dtype=np.uint32)
    b = np.array([15, 7], dtype=np.uint32)
    arr = np.array([[x1, x2] for x1, x2 in zip(a, b)])
    actual = fpair.pair(arr)
    expected = np.array([151,  62], dtype=np.uint64)
    assert all([x == y for x, y in zip(actual, expected)])


def test_unpair_arr():
    a = np.array([1, 3], dtype=np.uint32)
    b = np.array([15, 7], dtype=np.uint32)
    arr = np.array([[x1, x2] for x1, x2 in zip(a, b)])
    actual = fpair.unpair(np.array([151,  62], dtype=np.uint64))
    assert (all([x == y for x, y in zip(arr[:, 0], actual[:, 0])]) and
            all([x == y for x, y in zip(arr[:, 1], actual[:, 1])]))
