import pyreadr
import pandas as pd

from epygenetics.clocks.regression_clock import RegressionClock


class LinClock(RegressionClock):
    def __init__(self):
        cpgs_dict = pyreadr.read_r('../../../CpGs_data/Lin_CpGs.rda')
        cpgs = pd.DataFrame(cpgs_dict['Lin_CpGs'])
        super().__init__('Lin', cpgs, 'id', 'coef', 12.2169841)
