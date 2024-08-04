from typing import Optional

import pandas as pd

from epygenetics.clocks.base_clocks.regression_clock import RegressionClock


class BohlinClock(RegressionClock):
    def __init__(self) -> None:
        cpgs: Optional[pd.DataFrame] = pd.read_csv('data/CpGs/Bohlin_CpGs.csv')
        super().__init__('Bohlin', 'CpG', 'coef', 277.2421, cpgs)
