import pyreadr
import pandas as pd

from epygenetics.clocks.regression_clock import RegressionClock


class WeidnerClock(RegressionClock):
    def __init__(self):
        cpgs_dict = pyreadr.read_r('../../../CpGs_data/Weidner_CpGs.rda')
        df = pd.DataFrame(cpgs_dict['Weidner_CpGs'])
        cpgs = df.assign(Coefficient=[-64.57, -42.57, 75.15])
        super().__init__('Weidner', cpgs, 'Weidner_CpGs', 'Coefficient', 111.83)
