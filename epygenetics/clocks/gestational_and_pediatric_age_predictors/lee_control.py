import pandas as pd

from ..regression_clock import RegressionClock


class LeeControlClock(RegressionClock):
    def __init__(self):
        cpgs = pd.read_csv('../data/CpGs/LeeControl_CpGs.csv')
        super().__init__('LeeControl', cpgs, 'CpG', 'coef', 13.06182)
