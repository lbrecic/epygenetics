import pandas as pd
import pyreadr

from epygenetics.clocks.regression_clock import RegressionClock


class AlcoholMcCartneyClock(RegressionClock):
    def __init__(self):
        cpgs_dict = pyreadr.read_r('CpGs_data/Alcohol_CpGs.rda')
        cpgs = pd.DataFrame(cpgs_dict['Alcohol_CpGs'])
        super().__init__('Alcohol_McCartney', cpgs, 'CpG', 'Beta', 0)
