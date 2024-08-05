from typing import Optional

import pandas as pd

from epygenetics.clocks.base_clocks.mean_clock import MeanClock
from epygenetics.clocks.type import ClockType


class HypoClock(MeanClock):
    def __init__(self) -> None:
        cpgs: Optional[pd.DataFrame] = pd.read_csv('data/CpGs/hypoClock_CpGs.csv')
        super().__init__(Clocktype.HYPO_CLOCK, 'hypoClock_CpGs', cpgs)
