import math
import numpy as np

def log_loss(y_true: list, y_pred: list, eps: float = 1e-15) -> list:
    """
    Returns a list of loss values.
    """
    # Write code here
    y_pred = np.asarray(y_pred)
    y_true = np.asarray(y_true)
    p_hat = np.clip(y_pred, eps, 1-eps)
    loss = -(y_true*np.log(p_hat) + (1-y_true)* np.log(1-p_hat))
    return loss.tolist()
   