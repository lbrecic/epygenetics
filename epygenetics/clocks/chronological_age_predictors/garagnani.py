from typing import Optional

import pandas as pd

from epygenetics.clocks.base_clocks.linear_clock import LinearClock


class GaragnaniClock(LinearClock):
    def __init__(self) -> None:
        cpgs: Optional[pd.DataFrame] = pd.read_csv('data/CpGs/Garagnani_CpG.csv')
        super().__init__('Garagnani', 'Garagnani', cpgs)
