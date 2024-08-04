import pandas as pd
from typing import Optional

from epygenetics.clocks.base_clocks.regression_clock import RegressionClock


class LeeControlClock(RegressionClock):
    def __init__(self) -> None:
        cpgs: Optional[pd.DataFrame] = pd.read_csv('data/CpGs/LeeControl_CpGs.csv')
        super().__init__('LeeControl', 'CpG', 'coef', 13.06182, cpgs)
