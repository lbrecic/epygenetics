import pandas as pd
from typing import Optional

from epygenetics.clocks.base_clocks.regression_clock import RegressionClock


class LinClock(RegressionClock):
    def __init__(self) -> None:
        cpgs: Optional[pd.DataFrame] = pd.read_csv('data/CpGs/Lin_CpGs.csv')
        super().__init__('Lin', 'id', 'coef', 12.2169841, cpgs)
