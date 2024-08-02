import pandas as pd

from epygenetics.clocks.base_clocks.mean_clock import MeanClock


class HypoClock(MeanClock):
    def __init__(self):
        cpgs = pd.read_csv('data/CpGs/hypoClock_CpGs.csv')
        super().__init__('hypoClock', 'hypoClock_CpGs', cpgs)
