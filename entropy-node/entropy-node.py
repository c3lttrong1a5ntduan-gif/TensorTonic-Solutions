import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    count = {}
    
    for i in y:
        count[i] = count.get(i,0) + 1 
    y_np = np.array(y)
    total = y_np.shape[0]
    prob = np.array([i/total for i in count.values()])
    return -np.sum(prob*np.log2(prob))
    