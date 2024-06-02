import pyreadr
import pandas as pd

from epygenetics.clocks.regression_clock import RegressionClock


class ZhangClock(RegressionClock):
    def __init__(self):
        cpgs_dict = pyreadr.read_r('../../../CpGs_data/Zhang_10_CpG.rda')
        cpgs = pd.DataFrame(cpgs_dict['Zhang_10_CpG'])
        super().__init__('Zhang', cpgs, 'Marker', 'coef', 0)
