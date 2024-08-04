import pandas as pd
from typing import Optional

from epygenetics.clocks.base_clocks.regression_clock import RegressionClock


class PhenoAgeClock(RegressionClock):
    def __init__(self) -> None:
        cpgs: Optional[pd.DataFrame] = pd.read_csv('data/CpGs/PhenoAge_CpGs.csv')
        super().__init__('PhenoAge', 'CpG', 'Weight', 60.664, cpgs)
