from typing import Optional

import pandas as pd

from epygenetics.clocks.base_clocks.regression_clock import RegressionClock
from epygenetics.clocks.type import ClockType
from epygenetics.store import AbstractDataStore
from epygenetics.store.strategies import CSVDataStore


class MayneClock(RegressionClock):
    """
    A specific implementation of the `RegressionClock` for the Mayne clock.
    This clock predicts biological age based on DNA methylation data using predefined
    CpG sites and their associated regression coefficients.

    The CpG sites and regression coefficients are loaded from a CSV file during
    initialization.
    """

    def __init__(self) -> None:
        """
        Initializes the MayneClock object by loading the necessary CpG sites
        and regression coefficients from a CSV file and setting the intercept
        for the regression model.
        """
        store: AbstractDataStore = CSVDataStore('data/CpGs')
        cpgs: Optional[pd.DataFrame] = store.retrieve_methylation_data(ClockType.MAYNE)
        super().__init__(ClockType.MAYNE, 'CpG', 'coef', 24.99026, cpgs)
