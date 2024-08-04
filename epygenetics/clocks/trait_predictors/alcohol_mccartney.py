from typing import Optional

import pandas as pd

from epygenetics.clocks.base_clocks.regression_clock import RegressionClock


class AlcoholMcCartneyClock(RegressionClock):
    def __init__(self) -> None:
        cpgs: Optional[pd.DataFrame] = pd.read_csv('data/CpGs/Alcohol_CpGs.csv')
        super().__init__('Alcohol_McCartney', 'CpG', 'Beta', 0, cpgs)
