from abc import ABC, abstractmethod
from typing import Any, Optional, Tuple, Union

import numpy as np
import pandas as pd


class Clock(ABC):
    def __init__(self, name: str, marker_name: str, cpgs: Optional[pd.DataFrame] = None):
        self.name: str = name
        self.marker_name: str = marker_name
        self.cpgs: Optional[pd.DataFrame] = cpgs

    def load_cpgs_from_csv(self, path: str) -> None:
        self.cpgs = pd.read_csv(path)

    @abstractmethod
    def check_cpgs(self, dna_m: pd.DataFrame, cpg_imputation: Optional[pd.DataFrame], imputation: bool) -> Tuple[np.ndarray, bool]:
        pass

    @abstractmethod
    def calculate(self, common_cpgs: np.ndarray, cpg_check: Any, dna_m: pd.DataFrame, pheno: Optional[pd.DataFrame], imputation: bool) -> Union[pd.DataFrame, pd.Series]:
        pass

    def execute(self, dna_m: pd.DataFrame, pheno: Optional[pd.DataFrame] = None, cpg_imputation: Optional[pd.DataFrame] = None, imputation: bool = False) -> None:
        cpgs, cpg_check = self.check_cpgs(dna_m, cpg_imputation, imputation)
        result = self.calculate(cpgs, cpg_check, dna_m, pheno, imputation)
        print(result)
