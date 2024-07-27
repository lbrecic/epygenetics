import pandas as pd

from epygenetics.clocks.mean_clock import MeanClock


class EpiTOCClock(MeanClock):
    def __init__(self):
        cpgs = pd.read_csv('../../CpGs/EpiToc_CpGs.csv')
        super().__init__('EpiTOC', cpgs, 'EpiToc_CpGs')
