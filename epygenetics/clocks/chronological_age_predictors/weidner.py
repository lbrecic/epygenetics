import pandas as pd

from ..regression_clock import RegressionClock


class WeidnerClock(RegressionClock):
    def __init__(self):
        cpgs = pd.read_csv('../data/CpGs/Weidner_CpGs.csv')
        super().__init__('Weidner', cpgs, 'Weidner_CpGs', 'Coefficient', 111.83)
