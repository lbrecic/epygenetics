from typing import Optional

import pandas as pd

from epygenetics.clocks.base_clocks.regression_clock import RegressionClock
from epygenetics.clocks.type import ClockType


class PhenoAgeClock(RegressionClock):
    def __init__(self) -> None:
        cpgs: Optional[pd.DataFrame] = pd.read_csv('data/CpGs/PhenoAge_CpGs.csv')
        super().__init__(ClockType.PHENO_AGE, 'CpG', 'Weight', 60.664, cpgs)
