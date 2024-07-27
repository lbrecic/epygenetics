import pandas as pd

from epygenetics.clocks.regression_clock import RegressionClock


class VidalBraloClock(RegressionClock):
    def __init__(self):
        cpgs = pd.read_csv('../../../data/CpGs/VidalBralo_CpGs.csv')
        super().__init__('VidalBralo', cpgs, 'Marker', 'coef', 84.7)
