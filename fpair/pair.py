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


def pair(a, b):
    """
    Parameters
    ----------
    a : np.array
    b : np.array

    Returns
    -------
    z : np.array
    """
    arrsrt = np.array([[x[0], x[1]] if x[0] < x[1] else [x[1], x[0]] for x in zip(a, b)])
    return np.array([_pair(x[0], x[1]) for x in arrsrt], dtype=np.uint64)


def unpair(z):
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
    return a, b