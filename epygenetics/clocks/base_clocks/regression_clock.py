from typing import Optional, Tuple, Union

import numpy as np
import pandas as pd

from epygenetics.clocks.base_clocks.clock import Clock
from epygenetics.utils.mean_impute import mean_impute


class RegressionClock(Clock):
    def __init__(self, name: str, marker_name: str, coef_name: str, reg_coef: float, cpgs: Optional[pd.DataFrame] = None):
        super().__init__(name, marker_name, cpgs)
        self.coef_name: str = coef_name
        self.reg_coef: float = reg_coef

    def check_cpgs(self, dna_m: pd.DataFrame, cpg_imputation: Optional[pd.DataFrame], imputation: bool) -> Tuple[np.ndarray, bool]:
        common_cpgs: np.ndarray = np.intersect1d(self.cpgs[self.marker_name], dna_m.columns)
        cpg_check: bool = len(self.cpgs[self.marker_name]) == len(common_cpgs)

        if not cpg_check and imputation:
            if cpg_imputation is None:
                raise ValueError("Necessary CpG is missing and no imputation data provided!")

            # Impute missing CpG values
            print(f"Imputation of missing CpG Values occurred for {self.name}")
            for cpg in self.cpgs[self.marker_name]:
                if cpg not in dna_m.columns:
                    mean_val: Optional[float] = mean_impute(cpg_imputation)
                    if mean_val is None:
                        raise ValueError(f"No imputation value provided for missing CpG: {cpg}")
                    dna_m[cpg] = mean_val
            common_cpgs = self.cpgs[self.marker_name].values

        return common_cpgs, cpg_check

    def calculate(self, common_cpgs: np.ndarray, cpg_check: bool, dna_m: pd.DataFrame, pheno: Optional[pd.DataFrame], imputation: bool) -> Union[pd.DataFrame, pd.Series]:
        if cpg_check or imputation:
            beta_values: pd.DataFrame = dna_m[common_cpgs]
            coefficients: pd.Series = self.cpgs.set_index(self.marker_name).loc[common_cpgs, self.coef_name]
            tt: np.ndarray = np.dot(beta_values, coefficients) + self.reg_coef

            if pheno is not None:
                pheno[self.name] = tt
                return pheno
            else:
                return pd.Series(tt, index=dna_m.index)

        else:
            raise Exception("CpG Check failed and imputation is not enabled or feasible.")
