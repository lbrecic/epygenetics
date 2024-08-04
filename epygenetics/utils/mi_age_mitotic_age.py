import numpy as np
from scipy.optimize import minimize

from epygenetics.utils.mi_age_fr_2 import miage_fr2
from epygenetics.utils.mi_age_grr_2 import miage_grr2


def miage_mitotic_age(beta: np.ndarray, b: float, c: float, d: float) -> np.ndarray:
    """
    Estimate the MiAge using optimization to minimize the MiAge_fr2 for each patient.

    Parameters:
    beta : ndarray
        Methylation beta values matrix with samples as rows and CpG sites as columns.
    b, c, d : float
        Parameters of the MiAge model.

    Returns:
    ndarray
        Estimated mitotic age for each patient.
    """
    upperage = 10000
    lowerage = 10
    n = np.full(beta.shape[1], 500)  # initial guesses
    no_initial_n = 5

    # Minimize the objective function for each patient
    for j in range(beta.shape[1]):
        betaj = beta[:, j]

        # Try different starting points and take the best result
        results = []
        for jj in range(no_initial_n):
            init_n = lowerage + jj * (upperage - lowerage) / no_initial_n
            res = minimize(miage_fr2, init_n, args=(b, c, d, betaj), method='L-BFGS-B', jac=miage_grr2,
                           bounds=[(lowerage, upperage)], options={'factr': 1})
            if res.success:
                results.append(res)

        # Choose the best optimization result
        if results:
            best_result = min(results, key=lambda x: x.fun)
            n[j] = best_result.x  # update the best parameter found

    return n

# Example usage:
# Assuming beta, b, c, and d are defined:
# ages = miage_mitotic_age(beta, b, c, d)
