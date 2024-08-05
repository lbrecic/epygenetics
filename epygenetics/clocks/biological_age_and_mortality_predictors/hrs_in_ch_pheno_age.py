from typing import Optional

import pandas as pd

from epygenetics.clocks.base_clocks.regression_clock import RegressionClock
from epygenetics.clocks.type import ClockType


class HRSInCHPhenoAgeClock(RegressionClock):
    def __init__(self) -> None:
        cpgs: Optional[pd.DataFrame] = pd.read_csv('data/CpGs/HRSInCHPhenoAge_CpGs.csv')
        super().__init__(ClockType.HRS_IN_CH_PHENO_AGE, 'CpG', 'Weight', 52.8334080, cpgs)
