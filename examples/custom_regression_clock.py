from typing import Optional

import pandas as pd

from epygenetics.clocks.base_clocks.regression_clock import RegressionClock


class CustomRegressionClock(RegressionClock):
    def __init__(self) -> None:
        cpgs: Optional[pd.DataFrame] = pd.read_csv('../data/examples/exampleCpGs.csv')
        super().__init__("CustomRegressionClock", 'CpG', 'Coef', 0.333, cpgs)
