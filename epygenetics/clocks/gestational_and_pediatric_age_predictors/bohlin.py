import pandas as pd
import pyreadr

from epygenetics.clocks.regression_clock import RegressionClock


class BohlinClock(RegressionClock):
    def __init__(self):
        cpgs_dict = pyreadr.read_r('../../../CpGs_data/Bohlin_CpGs.rda')
        cpgs = pd.DataFrame(cpgs_dict['Bohlin_CpGs'])
        super().__init__('Bohlin', cpgs, 'CpG', 'coef', 277.2421)
