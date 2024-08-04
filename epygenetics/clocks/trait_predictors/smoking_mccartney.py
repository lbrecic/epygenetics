import pandas as pd
from typing import Optional

from epygenetics.clocks.base_clocks.regression_clock import RegressionClock


class SmokingMcCartneyClock(RegressionClock):
    def __init__(self) -> None:
        cpgs: Optional[pd.DataFrame] = pd.read_csv('data/CpGs/Smoking_CpGs.csv')
        super().__init__('Smoking_McCartney', 'CpG', 'Beta', 0, cpgs)
