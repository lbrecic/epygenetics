import pandas as pd

from ..regression_clock import RegressionClock


class BMIMcCartneyClock(RegressionClock):
    def __init__(self):
        cpgs = pd.read_csv('../data/CpGs/BMI_CpGs.csv')
        super().__init__('BMI_McCartney', cpgs, 'CpG', 'Beta', 0)
