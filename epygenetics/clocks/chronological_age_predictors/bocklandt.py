import pandas as pd
from typing import Optional

from epygenetics.clocks.base_clocks.linear_clock import LinearClock


class BocklandtClock(LinearClock):
    def __init__(self) -> None:
        cpgs: Optional[pd.DataFrame] = pd.read_csv('data/CpGs/Bocklandt_CpG.csv')
        super().__init__('Bocklandt', 'Bocklandt_CpG', cpgs)
