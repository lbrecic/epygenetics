from typing import Optional

import pandas as pd

from epygenetics.clocks.base_clocks.regression_clock import RegressionClock
from epygenetics.clocks.type import ClockType


class LeeRefinedRobustClock(RegressionClock):
    def __init__(self) -> None:
        cpgs: Optional[pd.DataFrame] = pd.read_csv('data/CpGs/LeeRefinedRobust_CpGs.csv')
        super().__init__(ClockType.LEE_REFINED_ROBUST, 'CpG', 'coef', 30.74966, cpgs)
