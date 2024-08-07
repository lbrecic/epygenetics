from abc import ABC, abstractmethod

import pandas as pd


class BaseImputer(ABC):
    @abstractmethod
    def impute(self, dna_m: pd.DataFrame) -> pd.DataFrame:
        pass
