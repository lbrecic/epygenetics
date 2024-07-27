import pandas as pd

from epygenetics.clocks.regression_clock import RegressionClock


class MayneClock(RegressionClock):
    def __init__(self):
        cpgs = pd.read_csv('../../CpGs/Mayne_CpGs.csv')
        super().__init__('Mayne', cpgs, 'CpG', 'coef', 24.99026)
