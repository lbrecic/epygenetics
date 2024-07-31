import pandas as pd

from ..regression_clock import RegressionClock


class LeeRobustClock(RegressionClock):
    def __init__(self):
        cpgs = pd.read_csv('../../../data/CpGs/LeeRobust_CpGs.csv')
        super().__init__('LeeRobust', cpgs, 'CpG', 'coef', 24.99772)
