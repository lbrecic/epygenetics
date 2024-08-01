import pandas as pd

from epygenetics.clocks.base_clocks.regression_clock import RegressionClock


class PRCPhenoAgeClock(RegressionClock):
    def __init__(self):
        cpgs = pd.read_csv('data/CpGs/prcPhenoAge_CpGs.csv')
        super().__init__('prcPhenoAge', cpgs, 'CpG', 'Weight', 0)
