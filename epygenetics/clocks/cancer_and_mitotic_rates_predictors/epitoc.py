from typing import Optional

import pandas as pd

from epygenetics.clocks.base_clocks.mean_clock import MeanClock
from epygenetics.clocks.type import ClockType


class EpiTOCClock(MeanClock):
    def __init__(self) -> None:
        cpgs: Optional[pd.DataFrame] = pd.read_csv('data/CpGs/EpiToc_CpGs.csv')
        super().__init__(ClockType.EPITOC, 'EpiToc_CpGs', cpgs)
