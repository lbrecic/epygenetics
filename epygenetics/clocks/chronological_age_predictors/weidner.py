import pandas as pd
from typing import Optional

from epygenetics.clocks.base_clocks.regression_clock import RegressionClock


class WeidnerClock(RegressionClock):
    def __init__(self) -> None:
        cpgs: Optional[pd.DataFrame] = pd.read_csv('data/CpGs/Weidner_CpGs.csv')
        super().__init__('Weidner', 'Weidner_CpGs', 'Coefficient', 111.83, cpgs)
