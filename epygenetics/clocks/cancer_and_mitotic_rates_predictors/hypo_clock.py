from typing import Optional

import pandas as pd

from epygenetics.clocks.base_clocks.mean_clock import MeanClock
from epygenetics.clocks.type import ClockType
from epygenetics.store import AbstractDataStore
from epygenetics.store.strategies import CSVDataStore


class HypoClock(MeanClock):
    """
    A specific implementation of the `MeanClock` for the HypoClock.
    This clock calculates the average methylation levels of specific CpG sites
    to estimate biological age or other outcomes.

    The CpG sites are loaded from a CSV file during initialization.
    """

    def __init__(self) -> None:
        """
        Initializes the HypoClock object by loading the necessary CpG sites
        from a CSV file.
        """
        store: AbstractDataStore = CSVDataStore('data/CpGs')
        cpgs: Optional[pd.DataFrame] = store.retrieve_methylation_data(ClockType.HYPO_CLOCK)
        super().__init__(ClockType.HYPO_CLOCK, 'hypoClock_CpGs', cpgs)
