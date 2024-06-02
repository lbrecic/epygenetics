import pandas as pd
import pyreadr

from epygenetics.clocks.mean_clock import MeanClock


class EpiTOCClock(MeanClock):
    def __init__(self):
        cpgs_dict = pyreadr.read_r('../../../CpGs_data/EpiToc_CpGs.rda')
        cpgs = pd.DataFrame(cpgs_dict['EpiToc_CpGs'])
        super().__init__('EpiTOC', cpgs, 'EpiToc_CpGs')
