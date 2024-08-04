import pandas as pd
from typing import Optional

from epygenetics.clocks.base_clocks.regression_clock import RegressionClock


class PRCPhenoAgeClock(RegressionClock):
    def __init__(self) -> None:
        cpgs: Optional[pd.DataFrame] = pd.read_csv('data/CpGs/prcPhenoAge_CpGs.csv')
        super().__init__('prcPhenoAge', 'CpG', 'Weight', 0, cpgs)
