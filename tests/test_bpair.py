import bpair
import numpy as np
from config import CONFIG


def test_pair():
    arr = np.array([[1, 15], [7, 3]], dtype='uint{0}'.format(CONFIG.UINT_SIZE_SM))
    actual = bpair.pair(arr)
    expected = np.array([4294967311, 12884901895], dtype='uint{0}'.format(CONFIG.UINT_SIZE_LG))
    assert all([x == y for x, y in zip(actual, expected)])


def test_unpair():
    expected = np.array([[1, 15], [3, 7]], dtype='uint{0}'.format(CONFIG.UINT_SIZE_SM))
    actual = bpair.unpair(np.array([4294967311, 12884901895], dtype='uint{0}'.format(CONFIG.UINT_SIZE_LG)))
    assert all([(expected[i][0] == actual[i][0]) and (expected[i][1] == actual[i][1]) for i in range(actual.shape[0])])
