import pandas as pd

from epygenetics.clocks.regression_clock import RegressionClock


class KnightClock(RegressionClock):
    def __init__(self):
        cpgs = pd.read_csv('../../CpGs/Knight_CpGs.csv')
        super().__init__('Knight', cpgs, 'CpG', 'coef', 41.7)
