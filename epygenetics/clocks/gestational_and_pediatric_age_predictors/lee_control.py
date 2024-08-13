from typing import Optional

import pandas as pd

from epygenetics.clocks.base_clocks.regression_clock import RegressionClock
from epygenetics.clocks.type import ClockType


class LeeControlClock(RegressionClock):
    """
    A specific implementation of the `RegressionClock` for the Lee Control clock.
    This clock predicts biological age based on DNA methylation data using predefined
    CpG sites and their associated regression coefficients.

    The CpG sites and regression coefficients are loaded from a CSV file during
    initialization.
    """

    def __init__(self) -> None:
        """
        Initializes the LeeControlClock object by loading the necessary CpG sites
        and regression coefficients from a CSV file and setting the intercept
        for the regression model.
        """
        cpgs: Optional[pd.DataFrame] = pd.read_csv('data/CpGs/LeeControl_CpGs.csv')
        super().__init__(ClockType.LEE_CONTROL, 'CpG', 'coef', 13.06182, cpgs)
