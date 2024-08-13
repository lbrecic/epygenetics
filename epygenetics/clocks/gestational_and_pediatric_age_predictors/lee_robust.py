from typing import Optional

import pandas as pd

from epygenetics.clocks.base_clocks.regression_clock import RegressionClock
from epygenetics.clocks.type import ClockType


class LeeRobustClock(RegressionClock):
    """
    A specific implementation of the `RegressionClock` for the Lee Robust clock.
    This clock predicts biological age based on DNA methylation data using predefined
    CpG sites and their associated regression coefficients.

    The CpG sites and regression coefficients are loaded from a CSV file during
    initialization.
    """

    def __init__(self) -> None:
        """
        Initializes the LeeRobustClock object by loading the necessary CpG sites
        and regression coefficients from a CSV file and setting the intercept
        for the regression model.
        """
        cpgs: Optional[pd.DataFrame] = pd.read_csv('data/CpGs/LeeRobust_CpGs.csv')
        super().__init__(ClockType.LEE_ROBUST, 'CpG', 'coef', 24.99772, cpgs)
