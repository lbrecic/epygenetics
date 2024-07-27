import pandas as pd

from epygenetics.clocks.regression_clock import RegressionClock


class LeeControlClock(RegressionClock):
    def __init__(self):
        cpgs = pd.read_csv('../../CpGs/LeeRobust_CpGs.csv')
        super().__init__('LeeRobust', cpgs, 'CpG', 'coef', 24.99772)
