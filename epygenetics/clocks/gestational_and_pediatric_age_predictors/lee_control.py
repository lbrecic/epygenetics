from typing import Optional

import pandas as pd

from epygenetics.clocks.base_clocks.regression_clock import RegressionClock
from epygenetics.clocks.type import ClockType


class LeeControlClock(RegressionClock):
    def __init__(self) -> None:
        cpgs: Optional[pd.DataFrame] = pd.read_csv('data/CpGs/LeeControl_CpGs.csv')
        super().__init__(ClockType.LEE_CONTROL, 'CpG', 'coef', 13.06182, cpgs)
