from typing import Optional

import pandas as pd

from epygenetics.clocks.base_clocks.regression_clock import RegressionClock
from epygenetics.clocks.type import ClockType


class VidalBraloClock(RegressionClock):
    def __init__(self) -> None:
        cpgs: Optional[pd.DataFrame] = pd.read_csv('data/CpGs/VidalBralo_CpGs.csv')
        super().__init__(ClockType.VIDAL_BRALO, 'Marker', 'coef', 84.7, cpgs)
