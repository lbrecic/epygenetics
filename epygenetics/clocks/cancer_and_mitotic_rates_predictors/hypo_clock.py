import pandas as pd
import pyreadr

from epygenetics.clocks.mean_clock import MeanClock


class HypoClock(MeanClock):
    def __init__(self):
        cpgs_dict = pyreadr.read_r('../../../CpGs_data/hypoClock_CpGs.rda')
        cpgs = pd.DataFrame(cpgs_dict['hypoClock_CpGs'])
        super().__init__('hypoClock', cpgs, 'hypoClock_CpGs')
