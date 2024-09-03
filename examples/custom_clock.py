from typing import Optional, Union, Tuple

import numpy as np
import pandas as pd

from epygenetics.clocks.base_clocks.clock import Clock
from epygenetics.imputers import ImputerType


class CustomClock(Clock):

    def __init__(self) -> None:
        cpgs: Optional[pd.DataFrame] = pd.read_csv('../data/examples/exampleCpGs.csv')
        super().__init__("CustomRegressionClock", 'CpG', 'Coef', 0.333, cpgs)

    def validate(self, dna_m: pd.DataFrame, is_imputation: bool = False, imputer_type=ImputerType.REGULAR,
                 cpg_imputation: Optional[pd.DataFrame] = None) -> Tuple[np.ndarray, bool]:
        pass

    def calculate(self, dna_m: pd.DataFrame, common_cpgs: np.ndarray, cpg_check: bool, pheno: Optional[pd.DataFrame],
                  is_imputation: bool) -> Union[pd.DataFrame, pd.Series]:
        pass
