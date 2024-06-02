import numpy as np

def miage_fr2(x, b, c, d, betaj):
    """
    Objective function used by the MiAge calculation to compute the sum of squared
    differences between observed methylation levels and a model prediction across CpG sites for a given patient.

    Parameters:
    x : array_like
        CpG positions or related indices.
    b : float
        Model parameter b.
    c : float
        Model parameter c.
    d : float
        Model parameter d.
    betaj : array_like
        Observed methylation levels for patient j.

    Returns:
    float
        Sum of squared differences for patient j.
    """
    nj = x
    return np.sum((c + b**(nj - 1) * d - betaj) ** 2, axis=None)  # Ensure na.rm equivalent by handling NaNs appropriately if needed.

# Example usage:
# Assuming x, b, c, d, and betaj are defined appropriately with numpy arrays or values:
# result = miage_fr2(x, b, c, d, betaj)
