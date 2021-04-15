import numpy as np
from config import CONFIG


def _pair(a, b):
    """
    Parameters
    ----------
    a : int
    b : int

    Returns
    -------
    z : int
    """
    return ((a + b) * (a + b + 1) // 2) + b


def pair(arr):
    """
    Parameters
    ----------
    arr : np.array of length two arrays

    Returns
    -------
    z : np.array
    """
    arrsrt = np.array([[x[0], x[1]] if (x[0] < x[1]) else [x[1], x[0]] for x in arr])
    return np.array([_pair(x[0], x[1]) for x in arrsrt], dtype='uint{0}'.format(CONFIG.UINT_SIZE_LG))


def _unpair(z):
    """
    Parameters
    ----------
    z : int

    Returns
    -------
    ab : list of length 2
    """
    w = int((np.sqrt(8 * z + 1) - 1) / 2)
    t = (w ** 2 + w) // 2 
    b = z - t
    a = w - b
    return [a, b]


def unpair(z):
    """
    Parameters
    ----------
    z : np.array

    Returns
    -------
    arr : np.array of length two arrays
    """
    return np.array([_unpair(idx) for idx in z], dtype='uint{0}'.format(CONFIG.UINT_SIZE_SM))
