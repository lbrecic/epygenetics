import pandas as pd
from typing import Optional

from epygenetics.clocks.base_clocks.mean_clock import MeanClock


class EpiTOCClock(MeanClock):
    def __init__(self) -> None:
        cpgs: Optional[pd.DataFrame] = pd.read_csv('data/CpGs/EpiToc_CpGs.csv')
        super().__init__('EpiTOC', 'EpiToc_CpGs', cpgs)
