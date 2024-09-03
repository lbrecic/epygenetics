from typing import Optional

import pandas as pd

from epygenetics.clocks.base_clocks.regression_clock import RegressionClock
from epygenetics.clocks.type import ClockType
from epygenetics.store import AbstractDataStore
from epygenetics.store.strategies import CSVDataStore


class PRCPhenoAgeClock(RegressionClock):
    """
    A specific implementation of the `RegressionClock` for the PRC PhenoAge clock.
    This clock predicts phenotypic age based on DNA methylation data using predefined
    CpG sites and their associated weights.

    The CpG sites and regression coefficients are loaded from a CSV file during
    initialization.
    """

    def __init__(self) -> None:
        """
        Initializes the PRCPhenoAgeClock object by loading the necessary CpG sites
        and weights from a CSV file and setting the intercept for the regression model.
        """
        store: AbstractDataStore = CSVDataStore('data/CpGs')
        cpgs: Optional[pd.DataFrame] = store.retrieve_methylation_data(ClockType.PRC_PHENO_AGE)
        super().__init__(ClockType.PRC_PHENO_AGE, 'CpG', 'Weight', 0, cpgs)
