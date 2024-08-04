from typing import Optional

import pandas as pd

from epygenetics.clocks.base_clocks.regression_clock import RegressionClock


class MayneClock(RegressionClock):
    def __init__(self) -> None:
        cpgs: Optional[pd.DataFrame] = pd.read_csv('data/CpGs/Mayne_CpGs.csv')
        super().__init__('Mayne', 'CpG', 'coef', 24.99026, cpgs)
