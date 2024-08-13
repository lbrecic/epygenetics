from typing import Optional

import pandas as pd

from epygenetics.clocks.base_clocks.regression_clock import RegressionClock
from epygenetics.clocks.type import ClockType


class NonPRCPhenoAgeClock(RegressionClock):
    """
    A specific implementation of the `RegressionClock` for the non-PRC PhenoAge clock.
    This clock predicts phenotypic age based on DNA methylation data using predefined
    CpG sites and their associated weights.

    The CpG sites and regression coefficients are loaded from a CSV file during
    initialization.
    """

    def __init__(self) -> None:
        """
        Initializes the NonPRCPhenoAgeClock object by loading the necessary CpG sites
        and weights from a CSV file and setting the intercept for the regression model.
        """
        cpgs: Optional[pd.DataFrame] = pd.read_csv('data/CpGs/non_prcPhenoAge_CpGs.csv')
        super().__init__(ClockType.NON_PRC_PHENO_AGE, 'CpG', 'Weight', 0, cpgs)
