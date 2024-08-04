import pandas as pd
from typing import Optional

from epygenetics.clocks.base_clocks.regression_clock import RegressionClock


class LeeRobustClock(RegressionClock):
    def __init__(self) -> None:
        cpgs: Optional[pd.DataFrame] = pd.read_csv('../data/CpGs/LeeRobust_CpGs.csv')
        super().__init__('LeeRobust', 'CpG', 'coef', 24.99772, cpgs)
