from typing import Optional

import pandas as pd

from epygenetics.clocks.base_clocks.regression_clock import RegressionClock
from epygenetics.clocks.type import ClockType


class HannumClock(RegressionClock):
    def __init__(self) -> None:
        cpgs: Optional[pd.DataFrame] = pd.read_csv('data/CpGs/Hannum_CpGs.csv')
        super().__init__(ClockType.HANNUM, 'Marker', 'Coefficient', 0, cpgs)
