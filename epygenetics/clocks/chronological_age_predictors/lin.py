import pandas as pd

from epygenetics.clocks.regression_clock import RegressionClock


class LinClock(RegressionClock):
    def __init__(self):
        cpgs = pd.read_csv('../../../data/CpGs/Lin_CpGs.csv')
        super().__init__('Lin', cpgs, 'id', 'coef', 12.2169841)
