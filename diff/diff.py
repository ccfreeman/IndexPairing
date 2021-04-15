import numpy as np


def diff(a, b, pmod, diff_pos='left'):
    """Return the pair-wise elements unique to one list (default left argument 'a'). Use the
    pairing function given as argument.
    
    Parameters
    ----------
    a : np.array
    b : np.array
    pmod : module with pair and unpair functions
    diff_pos : string ('left' or 'right')
        Whether we want the unique items from the left or right (a or b) to be returned.
    
    Returns
    -------
    z : np.array
    """
    if diff_pos == 'left':
        return pmod.unpair(np.setdiff1d(pmod.pair(a), pmod.pair(b)))
    if diff_pos == 'right':
        return pmod.unpair(np.setdiff1d(pmod.pair(b), pmod.pair(a)))