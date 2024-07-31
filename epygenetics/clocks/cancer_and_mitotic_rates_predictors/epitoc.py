import pandas as pd

from ..mean_clock import MeanClock


class EpiTOCClock(MeanClock):
    def __init__(self):
        cpgs = pd.read_csv('../data/CpGs/EpiToc_CpGs.csv')
        super().__init__('EpiTOC', cpgs, 'EpiToc_CpGs')
