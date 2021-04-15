import bpair
import fpair
from diff import diff
from config import CONFIG
import numpy as np

A = np.array([[1,15], [3,7]], dtype='uint{0}'.format(CONFIG.UINT_SIZE_SM))
B = np.array([[1,15], [7,4]], dtype='uint{0}'.format(CONFIG.UINT_SIZE_SM))

def test_bpair_diff_left():
    """ Test the difference between lists between both pairing functions. """
    expected = np.array([[3,7]], dtype='uint{0}'.format(CONFIG.UINT_SIZE_SM))
    actual = diff(A, B, bpair, diff_pos='left')
    assert all([(expected[i][0] == actual[i][0]) and (expected[i][1] == actual[i][1]) for i in range(expected.shape[0])])


def test_bpair_diff_right():
    """ Test the difference between lists between both pairing functions. """
    expected = np.array([[4,7]], dtype='uint{0}'.format(CONFIG.UINT_SIZE_SM))
    actual = diff(A, B, bpair, diff_pos='right')
    assert all([(expected[i][0] == actual[i][0]) and (expected[i][1] == actual[i][1]) for i in range(expected.shape[0])])


def test_fpair_diff_left():
    """ Test the difference between lists between both pairing functions. """
    expected = np.array([[3,7]], dtype='uint{0}'.format(CONFIG.UINT_SIZE_SM))
    actual = diff(A, B, fpair, diff_pos='left')
    assert all([(expected[i][0] == actual[i][0]) and (expected[i][1] == actual[i][1]) for i in range(expected.shape[0])])


def test_fpair_diff_right():
    """ Test the difference between lists between both pairing functions. """
    expected = np.array([[4,7]], dtype='uint{0}'.format(CONFIG.UINT_SIZE_SM))
    actual = diff(A, B, fpair, diff_pos='right')
    assert all([(expected[i][0] == actual[i][0]) and (expected[i][1] == actual[i][1]) for i in range(expected.shape[0])])
