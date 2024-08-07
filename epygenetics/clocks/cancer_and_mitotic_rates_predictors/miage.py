from typing import Any, Optional, Tuple, Union

import numpy as np
import pandas as pd

from epygenetics.clocks.base_clocks.regression_clock import RegressionClock
from epygenetics.clocks.type import ClockType
from epygenetics.utils.mi_age_mitotic_age import miage_mitotic_age


class MiAgeClock(RegressionClock):
    def __init__(self, *miage_params: Any) -> None:
        cpgs: Optional[pd.DataFrame] = pd.read_csv('data/CpGs/MiAge_CpGs.csv')
        super().__init__(ClockType.MIAGE, 'CpGs', 'Age-hyper/Age-hypo', 0, cpgs)
        self.miage_params: Tuple[Any, ...] = miage_params

    def calculate(self, dna_m: pd.DataFrame, common_cpgs: np.ndarray, cpg_check: bool, pheno: Optional[pd.DataFrame], is_imputation: bool) -> Union[pd.DataFrame, pd.Series]:
        if cpg_check or is_imputation:
            beta_values: pd.DataFrame = dna_m[common_cpgs]
            transposed_data: pd.DataFrame = beta_values.T  # Transpose data to match expected input format
            miage: np.ndarray = miage_mitotic_age(transposed_data, *self.miage_params)

            if pheno is not None:
                pheno[self.name] = miage
                return pheno
            else:
                return pd.Series(miage, index=dna_m.index)

        else:
            raise Exception("CpG Check failed and imputation is not enabled or feasible.")
