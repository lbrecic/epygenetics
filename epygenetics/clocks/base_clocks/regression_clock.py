from typing import Optional, Tuple, Union

import numpy as np
import pandas as pd

from epygenetics.clocks.base_clocks.clock import Clock
from epygenetics.imputers.base_imputer import BaseImputer
from epygenetics.imputers.factory import ImputerFactory
from epygenetics.imputers.type import ImputerType


class RegressionClock(Clock):
    def __init__(self, name: str, marker_name: str, coef_name: str, reg_coef: float,
                 cpgs: Optional[pd.DataFrame] = None):
        super().__init__(name, marker_name, cpgs)
        self.coef_name: str = coef_name
        self.reg_coef: float = reg_coef

    def check_cpgs(self, dna_m: pd.DataFrame, is_imputation: bool = False, imputer_type=ImputerType.REGULAR,
                   cpg_imputation: Optional[pd.DataFrame] = None) -> Tuple[np.ndarray, bool]:
        common_cpgs: np.ndarray = np.intersect1d(self.cpgs[self.marker_name], dna_m.columns)
        cpg_check: bool = len(self.cpgs[self.marker_name]) == len(common_cpgs)

        if not cpg_check and is_imputation:
            # Impute missing CpG values
            print(f"Imputation of missing CpG Values occurred for {self.name}")
            for cpg in self.cpgs[self.marker_name]:
                if cpg not in dna_m.columns:
                    dna_m[cpg] = np.nan

            imputer: BaseImputer = ImputerFactory.create_imputer(imputer_type, cpg_imputation)
            imputer.impute(dna_m)

            common_cpgs = self.cpgs[self.marker_name].values

        return common_cpgs, cpg_check

    def calculate(self, dna_m: pd.DataFrame, common_cpgs: np.ndarray, cpg_check: bool, pheno: Optional[pd.DataFrame],
                  is_imputation: bool) -> Union[pd.DataFrame, pd.Series]:
        if cpg_check or is_imputation:
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
