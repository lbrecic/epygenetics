from typing import Optional

import pandas as pd

from epygenetics.clocks.base_clocks.regression_clock import RegressionClock
from epygenetics.clocks.type import ClockType


class LinClock(RegressionClock):
    def __init__(self) -> None:
        cpgs: Optional[pd.DataFrame] = pd.read_csv('data/CpGs/Lin_CpGs.csv')
        super().__init__(ClockType.LIN, 'id', 'coef', 12.2169841, cpgs)
