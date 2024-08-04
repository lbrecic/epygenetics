from typing import Optional

import pandas as pd

from epygenetics.clocks.base_clocks.linear_clock import LinearClock


class BocklandtClock(LinearClock):
    def __init__(self) -> None:
        cpgs: Optional[pd.DataFrame] = pd.read_csv('data/CpGs/Bocklandt_CpG.csv')
        super().__init__('Bocklandt', 'Bocklandt_CpG', cpgs)
