import pandas as pd
import pyreadr

from epygenetics.clocks.regression_clock import RegressionClock


class LeeRefinedRobustClock(RegressionClock):
    def __init__(self):
        cpgs_dict = pyreadr.read_r('../../../CpGs_data/`LeeRefinedRobust`_CpGs.rda')
        cpgs = pd.DataFrame(cpgs_dict['LeeRefinedRobust_CpGs'])
        super().__init__('LeeRefinedRobust', cpgs, 'CpG', 'coef', 30.74966)
