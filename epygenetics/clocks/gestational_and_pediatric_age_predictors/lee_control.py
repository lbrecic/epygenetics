import pandas as pd
import pyreadr

from epygenetics.clocks.regression_clock import RegressionClock


class LeeControlClock(RegressionClock):
    def __init__(self):
        cpgs_dict = pyreadr.read_r('../../../CpGs_data/`LeeControl`_CpGs.rda')
        cpgs = pd.DataFrame(cpgs_dict['LeeControl_CpGs'])
        super().__init__('LeeControl', cpgs, 'CpG', 'coef', 13.06182)
