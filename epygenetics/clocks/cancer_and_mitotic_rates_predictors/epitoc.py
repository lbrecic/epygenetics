from typing import Optional

import pandas as pd

from epygenetics.clocks.base_clocks.mean_clock import MeanClock
from epygenetics.clocks.type import ClockType


class EpiTOCClock(MeanClock):
    """
    A specific implementation of the `MeanClock` for the EpiTOC clock.
    This clock calculates the average methylation levels of specific CpG sites
    to estimate biological age.

    The CpG sites are loaded from a CSV file during initialization.
    """

    def __init__(self) -> None:
        """
        Initializes the EpiTOCClock object by loading the necessary CpG sites
        from a CSV file.
        """
        cpgs: Optional[pd.DataFrame] = pd.read_csv('data/CpGs/EpiToc_CpGs.csv')
        super().__init__(ClockType.EPITOC, 'EpiToc_CpGs', cpgs)
