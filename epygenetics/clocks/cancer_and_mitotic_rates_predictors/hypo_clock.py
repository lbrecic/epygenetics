import pandas as pd

from epygenetics.clocks.mean_clock import MeanClock


class HypoClock(MeanClock):
    def __init__(self):
        cpgs = pd.read_csv('../../CpGs/hypoClock_CpGs.csv')
        super().__init__('hypoClock', cpgs, 'hypoClock_CpGs')
