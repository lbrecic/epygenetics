from typing import Optional

import pandas as pd

from epygenetics.clocks.base_clocks.regression_clock import RegressionClock
from epygenetics.clocks.type import ClockType


class MayneClock(RegressionClock):
    def __init__(self) -> None:
        cpgs: Optional[pd.DataFrame] = pd.read_csv('data/CpGs/Mayne_CpGs.csv')
        super().__init__(ClockType.MAYNE, 'CpG', 'coef', 24.99026, cpgs)
