from abc import ABC, abstractmethod
from typing import Any, Optional, Tuple, Union

import numpy as np
import pandas as pd

from epygenetics.imputers.type import ImputerType


class Clock(ABC):
    def __init__(self, name: str, marker_name: str, cpgs: Optional[pd.DataFrame] = None):
        self.name: str = name
        self.marker_name: str = marker_name
        self.cpgs: Optional[pd.DataFrame] = cpgs

    def load_cpgs_from_csv(self, path: str) -> None:
        self.cpgs = pd.read_csv(path)

    @abstractmethod
    def check_cpgs(self, dna_m: pd.DataFrame, is_imputation: bool = False, imputer_type=ImputerType.REGULAR, cpg_imputation: Optional[pd.DataFrame] = None) -> Tuple[np.ndarray, bool]:
        pass

    @abstractmethod
    def calculate(self, dna_m: pd.DataFrame, common_cpgs: np.ndarray, cpg_check: Any, pheno: Optional[pd.DataFrame], is_imputation: bool) -> Union[pd.DataFrame, pd.Series]:
        pass

    def execute(self, dna_m: pd.DataFrame, pheno: Optional[pd.DataFrame] = None, is_imputation: bool = False, imputation_type=ImputerType.REGULAR, cpg_imputation: Optional[pd.DataFrame] = None) -> None:
        cpgs, cpg_check = self.check_cpgs(dna_m, is_imputation, imputation_type, cpg_imputation)
        result = self.calculate(dna_m, cpgs, cpg_check, pheno, is_imputation)
        print(result)
