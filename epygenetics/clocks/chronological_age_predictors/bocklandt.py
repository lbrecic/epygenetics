import pyreadr
import pandas as pd

from masters_thesis.epygenetics.clocks.linear_clock import LinearClock


class BocklandtClock(LinearClock):
    def __init__(self):
        cpgs_dict = pyreadr.read_r('CpGs_data/Bocklandt_CpG.rda')
        cpgs = pd.DataFrame(cpgs_dict['Bocklandt_CpG'])
        super().__init__('Bocklandt', cpgs, 'Bocklandt_CpG')