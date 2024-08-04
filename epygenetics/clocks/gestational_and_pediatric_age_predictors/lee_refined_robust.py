import pandas as pd
from typing import Optional

from epygenetics.clocks.base_clocks.regression_clock import RegressionClock


class LeeRefinedRobustClock(RegressionClock):
    def __init__(self) -> None:
        cpgs: Optional[pd.DataFrame] = pd.read_csv('data/CpGs/LeeRefinedRobust_CpGs.csv')
        super().__init__('LeeRefinedRobust', 'CpG', 'coef', 30.74966, cpgs)
