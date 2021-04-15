import numpy as np

def diff(a, b, pair_func, diff_pos='left'):
    """Return the pair-wise elements unique to one list (default left argument 'a'). Use the
    pairing function given as argument.
    
    Parameters
    ----------
    a : np.array
    b : np.array
    pair_func : function
    
    Returns
    -------
    z : np.array
    """
    if diff_pos == 'left':
        return a[~np.in1d(pair_func(a), pair_func(b))]
    return b[~np.in1d(pair_func(a), pair_func(b))]
