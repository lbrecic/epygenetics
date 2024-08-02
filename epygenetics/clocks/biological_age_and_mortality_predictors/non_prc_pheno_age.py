import pandas as pd

from epygenetics.clocks.base_clocks.regression_clock import RegressionClock


class NonPRCPhenoAgeClock(RegressionClock):
    def __init__(self):
        cpgs = pd.read_csv('data/CpGs/non_prcPhenoAge_CpGs.csv')
        super().__init__('non_prcPhenoAge','CpG', 'Weight', 0, cpgs)
