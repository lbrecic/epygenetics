from typing import Optional

import pandas as pd

from epygenetics.clocks.base_clocks.regression_clock import RegressionClock
from epygenetics.clocks.type import ClockType


class ZhangClock(RegressionClock):
    def __init__(self) -> None:
        cpgs: Optional[pd.DataFrame] = pd.read_csv('data/CpGs/Zhang_10_CpG.csv')
        super().__init__(ClockType.ZHANG, 'Marker', 'coef', 0, cpgs)
