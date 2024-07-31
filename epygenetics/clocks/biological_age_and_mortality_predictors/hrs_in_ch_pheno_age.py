import pandas as pd

from ..regression_clock import RegressionClock


class HRSInCHPhenoAgeClock(RegressionClock):
    def __init__(self):
        cpgs = pd.read_csv('../data/CpGs/HRSInCHPhenoAge_CpGs.csv')
        super().__init__('HRSInChPhenoAge', cpgs, 'CpG', 'Weight', 52.8334080)
