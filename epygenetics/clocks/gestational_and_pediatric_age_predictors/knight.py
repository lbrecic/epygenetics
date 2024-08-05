from typing import Optional

import pandas as pd

from epygenetics.clocks.base_clocks.regression_clock import RegressionClock
from epygenetics.clocks.type import ClockType


class KnightClock(RegressionClock):
    def __init__(self) -> None:
        cpgs: Optional[pd.DataFrame] = pd.read_csv('data/CpGs/Knight_CpGs.csv')
        super().__init__(ClockType.KNIGHT, 'CpG', 'coef', 41.7, cpgs)
