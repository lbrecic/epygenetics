import pandas as pd
import pyreadr

from epygenetics.clocks.regression_clock import RegressionClock


class KnightClock(RegressionClock):
    def __init__(self):
        cpgs_dict = pyreadr.read_r('../../../CpGs_data/Knight_CpGs.rda')
        cpgs = pd.DataFrame(cpgs_dict['Knight_CpGs'])
        super().__init__('Knight', cpgs, 'CpG', 'coef', 41.7)
