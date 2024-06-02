import pandas as pd
import pyreadr

from epygenetics.clocks.regression_clock import RegressionClock


class HannumClock(RegressionClock):
    def __init__(self):
        cpgs_dict = pyreadr.read_r('../../../CpGs_data/Hannum_CpGs.rda')
        cpgs = pd.DataFrame(cpgs_dict['Hannum_CpGs'])
        super().__init__('Hannum', cpgs, 'Marker', 'Coefficient', 0)
