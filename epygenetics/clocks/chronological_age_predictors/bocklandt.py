from typing import Optional

import pandas as pd

from epygenetics.clocks.base_clocks.linear_clock import LinearClock
from epygenetics.clocks.type import ClockType
from epygenetics.store import AbstractDataStore
from epygenetics.store.strategies import CSVDataStore


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
        store: AbstractDataStore = CSVDataStore('data/CpGs')
        cpgs: Optional[pd.DataFrame] = store.retrieve_methylation_data(ClockType.BOCKLANDT)
        super().__init__(ClockType.BOCKLANDT, 'Bocklandt_CpG', cpgs)
