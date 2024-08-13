from typing import Optional

import pandas as pd

from epygenetics.clocks.base_clocks.linear_clock import LinearClock
from epygenetics.clocks.type import ClockType


class BocklandtClock(LinearClock):
    """
    A specific implementation of the `LinearClock` for the Bocklandt clock.
    This clock predicts biological age based on the methylation status of specific CpG sites.

    The CpG sites are loaded from a CSV file during initialization.
    """

    def __init__(self) -> None:
        """
        Initializes the BocklandtClock object by loading the necessary CpG sites
        from a CSV file.
        """
        cpgs: Optional[pd.DataFrame] = pd.read_csv('data/CpGs/Bocklandt_CpG.csv')
        super().__init__(ClockType.BOCKLANDT, 'Bocklandt_CpG', cpgs)
