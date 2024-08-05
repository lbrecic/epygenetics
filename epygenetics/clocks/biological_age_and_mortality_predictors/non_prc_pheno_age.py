from typing import Optional

import pandas as pd

from epygenetics.clocks.base_clocks.regression_clock import RegressionClock
from epygenetics.clocks.type import ClockType


class NonPRCPhenoAgeClock(RegressionClock):
    def __init__(self) -> None:
        cpgs: Optional[pd.DataFrame] = pd.read_csv('data/CpGs/non_prcPhenoAge_CpGs.csv')
        super().__init__(ClockType.NON_PRC_PHENO_AGE, 'CpG', 'Weight', 0, cpgs)
