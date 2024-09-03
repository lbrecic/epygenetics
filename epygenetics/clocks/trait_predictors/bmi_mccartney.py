from typing import Optional

import pandas as pd

from epygenetics.clocks.base_clocks.regression_clock import RegressionClock
from epygenetics.clocks.type import ClockType
from epygenetics.store import AbstractDataStore
from epygenetics.store.strategies import CSVDataStore


class BMIMcCartneyClock(RegressionClock):
    """
    A specific implementation of the `RegressionClock` for the BMI McCartney clock.
    This clock predicts biological age or BMI-related phenotypic outcomes based on DNA
    methylation data using predefined CpG sites and their associated regression coefficients.

    The CpG sites and regression coefficients are loaded from a CSV file during
    initialization.
    """

    def __init__(self) -> None:
        """
        Initializes the BMIMcCartneyClock object by loading the necessary CpG sites
        and regression coefficients from a CSV file and setting the intercept
        for the regression model.
        """
        store: AbstractDataStore = CSVDataStore('data/CpGs')
        cpgs: Optional[pd.DataFrame] = store.retrieve_methylation_data(ClockType.BMI_MCCARTNEY)
        super().__init__(ClockType.BMI_MCCARTNEY, 'CpG', 'Beta', 0, cpgs)
