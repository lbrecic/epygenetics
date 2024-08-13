from typing import Union

import numpy as np


def miage_fr2(x: Union[np.ndarray, float], b: float, c: float, d: float, betaj: np.ndarray) -> float:
    """
    Objective function used by the MiAge calculation to compute the sum of squared
    differences between observed methylation levels and a model prediction across CpG sites for a given patient.

    Parameters:
        x (Union[np.ndarray, float]): CpG positions or related indices.
        b (float): Model parameter b.
        c (float): Model parameter c.
        d (float): Model parameter d.
        betaj (np.ndarray): Observed methylation levels for patient j.

    Returns:
        float: Sum of squared differences for patient j.
    """
    nj = x
    return np.sum((c + b ** (nj - 1) * d - betaj) ** 2, axis=None)
