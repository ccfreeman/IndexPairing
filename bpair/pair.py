import numpy as np
from config import CONFIG

def pair(arr):
    """
    Parameters
    ----------
    a : np.array of uint32
    b : np.array of uint32
    
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
    a : np.array of uint32
    b : np.array of uint32
    """
    a = (z >> CONFIG.N_BITSHIFT).astype('uint{0}'.format(CONFIG.UINT_SIZE_SM))
    b = z.astype('uint{0}'.format(CONFIG.UINT_SIZE_SM))
    return np.column_stack((a, b))
