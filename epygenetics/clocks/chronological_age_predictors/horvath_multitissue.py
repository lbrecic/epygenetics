from typing import Optional, Union

import numpy as np
import pandas as pd

from epygenetics.clocks.base_clocks.regression_clock import RegressionClock
from epygenetics.utils.anti_trafo import anti_trafo


class HorvathMultitissueClock(RegressionClock):
    def __init__(self):
        cpgs: pd.DataFrame = pd.read_csv('data/CpGs/Horvath1_CpGs.csv')
        super().__init__('Horvath1', 'CpGmarker', 'CoefficientTraining', 0.696, cpgs)

    def calculate(self, common_cpgs: np.ndarray, cpg_check: bool, dna_m: pd.DataFrame, pheno: Optional[pd.DataFrame], imputation: bool) -> Union[pd.DataFrame, pd.Series]:
        if cpg_check or imputation:
            beta_values: pd.DataFrame = dna_m[common_cpgs]
            coefficients: pd.Series = self.cpgs.set_index(self.marker_name).loc[common_cpgs, self.coef_name]
            tt: np.ndarray = np.dot(beta_values, coefficients) + self.reg_coef
            horvath1: np.ndarray = anti_trafo(tt)

            if pheno is not None:
                pheno[self.name] = horvath1
                return pheno
            else:
                return pd.Series(horvath1, index=dna_m.index)

        else:
            raise Exception("CpG Check failed and imputation is not enabled or feasible.")
