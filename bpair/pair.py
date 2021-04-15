import numpy as np
from config import CONFIG

def pair(arr):
    """
    Parameters
    ----------
    arr : np.array of length two arrays
    
    Returns
    -------
    z : np.array of uint64
    """
    arrsrt = np.array([[x[0], x[1]] if (x[0] < x[1]) else [x[1], x[0]] for x in arr], dtype='uint{0}'.format(CONFIG.UINT_SIZE_SM))
    return (arrsrt[:, 0].astype('uint{0}'.format(CONFIG.UINT_SIZE_LG)) << CONFIG.N_BITSHIFT) + arrsrt[:, 1].astype('uint{0}'.format(CONFIG.UINT_SIZE_LG))


def unpair(z):
    """
    Parameters
    ----------
    z : np.array of uint64
    
    Returns
    -------
    arr : np.array of length two arrays
    """
    a = (z >> CONFIG.N_BITSHIFT).astype('uint{0}'.format(CONFIG.UINT_SIZE_SM))
    b = z.astype('uint{0}'.format(CONFIG.UINT_SIZE_SM))
    return np.column_stack((a, b))
