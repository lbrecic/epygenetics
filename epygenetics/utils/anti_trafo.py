from typing import Union

import numpy as np


def anti_trafo(x: Union[np.ndarray, float], adult_age: int = 20) -> Union[np.ndarray, float]:
    """
    Reverse the transformation applied to ages, restoring them to their original scale.

    This function applies an inverse transformation to previously transformed age data. It uses
    an exponential adjustment for negative values and a linear adjustment for non-negative values.
    This approach attempts to estimate the original ages from transformed data.

    Parameters:
    x : A vector of sample ages, which have been transformed by some prior function.
    adult_age : The age considered to be the cutoff for adulthood, used to determine scaling factors.

    Returns:
    A vector representing the restored, original ages based on the inverse of the applied transformations.
    """
    # Apply exponential transformation for x < 0, and linear transformation for x >= 0
    # These transformations are designed to revert any prior adjustments made to the age data
    y = np.where(x < 0, (1 + adult_age) * np.exp(x) - 1, (1 + adult_age) * x + adult_age)

    return y
