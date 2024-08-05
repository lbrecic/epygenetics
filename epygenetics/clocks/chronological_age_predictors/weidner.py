from typing import Optional

import pandas as pd

from epygenetics.clocks.base_clocks.regression_clock import RegressionClock
from epygenetics.clocks.type import ClockType


class WeidnerClock(RegressionClock):
    def __init__(self) -> None:
        cpgs: Optional[pd.DataFrame] = pd.read_csv('data/CpGs/Weidner_CpGs.csv')
        super().__init__(ClockType.WEIDNER, 'Weidner_CpGs', 'Coefficient', 111.83, cpgs)
