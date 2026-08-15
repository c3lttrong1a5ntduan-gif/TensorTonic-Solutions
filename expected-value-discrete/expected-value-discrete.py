import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    
    x = np.array(x)
    p = np.array(p)
    if np.sum(p) != 1 :
        raise ValueError("Sum of probabilities must be 1")
    if x.shape[0] != p.shape[0]:
        raise ValueError("Not the same shape")
    
    return np.sum(x*p)
    
