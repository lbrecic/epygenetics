import numpy as np
from typing import Union


def trafo(x: Union[np.ndarray, float], adult_age: int = 20) -> Union[np.ndarray, float]:
    """
    Transform a vector of sample ages based on a logarithmic or linear scaling.

    This function applies a transformation to age data, adjusting it using a logarithmic scale
    for values at or below the threshold of adulthood, and a linear scale above this threshold.
    This models the perception of age where younger ages (below adulthood) undergo more perceptible
    changes than older ages.

    Parameters:
    x : A vector of sample ages.
    adult_age : The threshold of adulthood, default is 20 years, which differentiates the type of scaling applied.

    Returns:
    A vector of transformed ages. Logarithmic scaling is applied to ages at or below the adulthood
    threshold, and linear scaling is applied to ages above this threshold.
    """
    # Normalize ages by the threshold of adulthood plus one to ensure proper scaling from zero
    x = (x + 1) / (1 + adult_age)

    # Apply a logarithmic transformation to normalized ages ≤ 1, and a linear adjustment (x-1) for normalized ages > 1
    y = np.where(x <= 1, np.log(x), x - 1)

    return y
