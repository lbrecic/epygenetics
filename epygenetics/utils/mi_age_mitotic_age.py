import numpy as np
from scipy.optimize import minimize

from epygenetics.utils.mi_age_fr_2 import miage_fr2
from epygenetics.utils.mi_age_grr_2 import miage_grr2


def miage_mitotic_age(beta: np.ndarray, b: float = 0.5, c: float = 0.5, d: float = 0.5) -> np.ndarray:
    """
    Estimate the mitotic age (MiAge) for each patient by optimizing the MiAge_fr2 objective function.

    Parameters:
        beta (np.ndarray): Methylation beta values matrix with samples as rows and CpG sites as columns.
        b (float): Parameter b of the MiAge model. Defaults to 0.5.
        c (float): Parameter c of the MiAge model. Defaults to 0.5.
        d (float): Parameter d of the MiAge model. Defaults to 0.5.

    Returns:
        np.ndarray: Estimated mitotic age for each patient.
    """
    upperage = 10000
    lowerage = 10
    n = np.full(beta.shape[1], 500)  # initial guesses for mitotic age
    no_initial_n = 5

    # Minimize the objective function for each CpG site (patient)
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
