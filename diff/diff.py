import numpy as np


def diff(a, b, pair_fnc, diff_pos='left'):
    """Return the pair-wise elements unique to one list (default left argument 'a'). Use the
    pairing function given as argument.
    
    Parameters
    ----------
    a : np.array
    b : np.array
    pair_fnc : function
    diff_pos : string ('left' or 'right')
        Whether we want the unique items from the left or right (a or b) to be returned.
    
    Returns
    -------
    z : np.array
    """
    if diff_pos == 'left':
        return a[~np.in1d(pair_fnc(a), pair_fnc(b))]
    return b[~np.in1d(pair_fnc(b), pair_fnc(a))]
