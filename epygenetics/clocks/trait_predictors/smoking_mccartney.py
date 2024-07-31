import pandas as pd

from ..regression_clock import RegressionClock


class SmokingMcCartneyClock(RegressionClock):
    def __init__(self):
        cpgs = pd.read_csv('../data/CpGs/Smoking_CpGs.csv')
        super().__init__('Smoking_McCartney', cpgs, 'CpG', 'Beta', 0)
