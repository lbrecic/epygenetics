from typing import Optional, Union

import numpy as np
import pandas as pd

from epygenetics.clocks.base_clocks.regression_clock import RegressionClock
from epygenetics.clocks.type import ClockType
from epygenetics.utils.anti_trafo import anti_trafo


class HorvathSkinAndBloodClock(RegressionClock):
    def __init__(self) -> None:
        cpgs: Optional[pd.DataFrame] = pd.read_csv('data/CpGs/Horvath2_CpGs.csv')
        super().__init__(ClockType.HORVATH_SKIN_AND_BLOOD, 'ID', 'Coef', -0.447119319, cpgs)

    def calculate(self, dna_m: pd.DataFrame, common_cpgs: np.ndarray, cpg_check: bool, pheno: Optional[pd.DataFrame], is_imputation: bool) -> Union[pd.DataFrame, pd.Series]:
        if cpg_check or is_imputation:
            beta_values: pd.DataFrame = dna_m[common_cpgs]
            coefficients: pd.Series = self.cpgs.set_index(self.marker_name).loc[common_cpgs, self.coef_name]
            tt: np.ndarray = np.dot(beta_values, coefficients) + self.reg_coef
            horvath_skin_and_blood: np.ndarray = anti_trafo(tt)

            if pheno is not None:
                pheno[self.name] = horvath_skin_and_blood
                return pheno
            else:
                return pd.Series(horvath_skin_and_blood, index=dna_m.index)

        else:
            raise Exception("CpG Check failed and imputation is not enabled or feasible.")
