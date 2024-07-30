import pandas as pd

from epygenetics.clocks.regression_clock import RegressionClock


class HRSInChPhenoAgeClock(RegressionClock):
    def __init__(self):
        cpgs = pd.read_csv('../../../data/CpGs/HRSInCHPhenoAge_CpGs.csv')
        super().__init__('HRSInChPhenoAge', cpgs, 'CpG', 'Weight', 52.8334080)
