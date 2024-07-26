import pandas as pd
import pyreadr

from epygenetics.clocks.regression_clock import RegressionClock


class MayneClock(RegressionClock):
    def __init__(self):
        cpgs_dict = pyreadr.read_r('../../../CpGs_data/`Mayne`_CpGs.rda')
        cpgs = pd.DataFrame(cpgs_dict['Mayne_CpGs'])
        super().__init__('Mayne', cpgs, 'CpG', 'coef', 24.99026)
