import numpy as np


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
    a : np.array
    b : np.array

    Returns
    -------
    z : np.array
    """
    arrsrt = np.array([[x[0], x[1]] if (x[0] < x[1]) else [x[1], x[0]] for x in arr])
    return np.array([_pair(x[0], x[1]) for x in arrsrt], dtype=np.uint64)


def _unpair(z):
    """
    Parameters
    ----------
    z : int

    Returns
    -------
    a : int
    b : int
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
    a : np.array
    b : np.array
    """
    return np.array([_unpair(idx) for idx in z], dtype=np.uint64)
