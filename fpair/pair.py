import numpy as np

def pair(a, b):
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