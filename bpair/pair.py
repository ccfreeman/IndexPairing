import numpy as np

N_BITSHIFT = 32

def pair(a, b):
    """
    Parameters
    ----------
    a : np.array of uint32
    b : np.array of uint32
    
    Returns
    -------
    z : np.array of uint64
    """
    return (a.astype(np.uint64) << N_BITSHIFT) + b.astype(np.uint64)


def unpair(z):
    """
    Parameters
    ----------
    z : np.array of uint64
    
    Returns
    -------
    a : np.array of uint32
    b : np.array of uint32
    """
    a = (z >> N_BITSHIFT).astype(np.uint32)
    b = z.astype(np.uint32)
    return a, b
