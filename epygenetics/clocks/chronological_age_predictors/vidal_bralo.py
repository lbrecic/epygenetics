import pyreadr
import pandas as pd

from epygenetics.clocks.regression_clock import RegressionClock


class VidalBraloClock(RegressionClock):
    def __init__(self):
        cpgs_dict = pyreadr.read_r('../../../CpGs_data/VidalBralo_CpGs.rda')
        cpgs = pd.DataFrame(cpgs_dict['VidalBralo_CpGs'])
        super().__init__('VidalBralo', cpgs, 'Marker', 'coef', 84.7)
