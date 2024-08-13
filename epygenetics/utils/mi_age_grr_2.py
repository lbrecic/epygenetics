from typing import Union

import numpy as np


def miage_grr2(x: Union[np.ndarray, float], b: float, c: float, d: float, betaj: np.ndarray) -> float:
    """
    Calculate the derivative of the objective function used by the MiAge calculation with respect to n_j.
    This derivative helps in optimization algorithms where gradients are required.

    Parameters:
        x (Union[np.ndarray, float]): CpG positions or related indices.
        b (float): Model parameter b.
        c (float): Model parameter c.
        d (float): Model parameter d.
        betaj (np.ndarray): Observed methylation levels for patient j.

    Returns:
        float: The gradient of the objective function with respect to n_j.
    """
    nj = x
    # Calculate the derivative component
    gradient = 2 * np.sum((c + b ** (nj - 1) * d - betaj) * b ** (nj - 1) * np.log(b) * d)
    return gradient
