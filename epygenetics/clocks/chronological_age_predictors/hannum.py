import pandas as pd
from typing import Optional

from epygenetics.clocks.base_clocks.regression_clock import RegressionClock


class HannumClock(RegressionClock):
    def __init__(self) -> None:
        cpgs: Optional[pd.DataFrame] = pd.read_csv('data/CpGs/Hannum_CpGs.csv')
        super().__init__('Hannum', 'Marker', 'Coefficient', 0, cpgs)
