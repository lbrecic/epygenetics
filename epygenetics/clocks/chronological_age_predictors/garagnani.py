import pandas as pd

from ..linear_clock import LinearClock


class GaragnaniClock(LinearClock):
    def __init__(self):
        cpgs = pd.read_csv('../data/CpGs/Garagnani_CpG.csv')
        super().__init__('Garagnani', cpgs, 'Garagnani')