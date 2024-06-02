import pyreadr
import pandas as pd

from epygenetics.clocks.linear_clock import LinearClock


class GaragnaniClock(LinearClock):
    def __init__(self):
        cpgs_dict = pyreadr.read_r('../../../CpGs_data/Garagnani_CpG.rda')
        cpgs = pd.DataFrame(cpgs_dict['Garagnani_CpG'])
        super().__init__('Garagnani', cpgs, 'Garagnani')