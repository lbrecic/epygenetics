import pandas as pd

from ..regression_clock import RegressionClock


class BohlinClock(RegressionClock):
    def __init__(self):
        cpgs = pd.read_csv('../data/CpGs/Bohlin_CpGs.csv')
        super().__init__('Bohlin', cpgs, 'CpG', 'coef', 277.2421)
