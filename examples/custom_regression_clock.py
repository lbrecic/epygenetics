from typing import Optional
import pandas as pd
from epygenetics.clocks.base_clocks.regression_clock import RegressionClock


class CustomRegressionClock(RegressionClock):
    def __init__(self, cpgs: Optional[pd.DataFrame] = None) -> None:
        super().__init__("CustomRegressionClock", 'CpG', 'Coef', 0.333, cpgs)
