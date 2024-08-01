import pandas as pd

from epygenetics.clocks.base_clocks.regression_clock import RegressionClock


class HannumClock(RegressionClock):
    def __init__(self):
        cpgs = pd.read_csv('data/CpGs/Hannum_CpGs.csv')
        super().__init__('Hannum', cpgs, 'Marker', 'Coefficient', 0)
