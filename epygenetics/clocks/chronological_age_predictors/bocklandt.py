import pandas as pd

from epygenetics.clocks.linear_clock import LinearClock


class BocklandtClock(LinearClock):
    def __init__(self):
        cpgs = pd.read_csv('../../CpGs/Bocklandt_CpG.csv')
        super().__init__('Bocklandt', cpgs, 'Bocklandt_CpG')