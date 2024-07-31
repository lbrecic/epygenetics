import pandas as pd

from ..regression_clock import RegressionClock


class MayneClock(RegressionClock):
    def __init__(self):
        cpgs = pd.read_csv('../data/CpGs/Mayne_CpGs.csv')
        super().__init__('Mayne', cpgs, 'CpG', 'coef', 24.99026)
