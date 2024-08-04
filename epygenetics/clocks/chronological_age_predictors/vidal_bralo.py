import pandas as pd
from typing import Optional

from epygenetics.clocks.base_clocks.regression_clock import RegressionClock


class VidalBraloClock(RegressionClock):
    def __init__(self) -> None:
        cpgs: Optional[pd.DataFrame] = pd.read_csv('data/CpGs/VidalBralo_CpGs.csv')
        super().__init__('VidalBralo', 'Marker', 'coef', 84.7, cpgs)
