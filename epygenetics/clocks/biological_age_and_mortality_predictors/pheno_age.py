import pandas as pd

from epygenetics.clocks.base_clocks.regression_clock import RegressionClock


class PhenoAgeClock(RegressionClock):
    def __init__(self):
        cpgs = pd.read_csv('data/CpGs/PhenoAge_CpGs.csv')
        super().__init__('PhenoAge', cpgs, 'CpG', 'Weight', 60.664)
