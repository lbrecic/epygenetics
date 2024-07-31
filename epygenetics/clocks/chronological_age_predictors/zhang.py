import pandas as pd

from ..regression_clock import RegressionClock


class ZhangClock(RegressionClock):
    def __init__(self):
        cpgs = pd.read_csv('../data/CpGs/Zhang_10_CpG.csv')
        super().__init__('Zhang', cpgs, 'Marker', 'coef', 0)
