from typing import Optional, Tuple, Union

import numpy as np
import pandas as pd

from epygenetics.clocks.base_clocks.clock import Clock
from epygenetics.imputers.type import ImputerType
from epygenetics.imputers.base_imputer import BaseImputer
from epygenetics.imputers.factory import ImputerFactory


class LinearClock(Clock):
    def check_cpgs(self, dna_m: pd.DataFrame, is_imputation: bool = False, imputer_type=ImputerType.REGULAR, cpg_imputation: Optional[pd.DataFrame] = None) -> Tuple[np.ndarray, bool]:
        if self.cpgs is None:
            raise ValueError("CpGs not loaded.")

        present_cpgs: np.ndarray = np.intersect1d(self.cpgs[self.marker_name], dna_m.columns)
        cpg_check: bool = len(self.cpgs[self.marker_name]) == len(present_cpgs)

        if not cpg_check and is_imputation:
            # Impute missing CpG values
            print(f"Imputation of missing CpG Values occurred for {self.name}")
            for cpg in self.cpgs[self.marker_name]:
                if cpg not in dna_m.columns:
                    dna_m[cpg] = np.nan

            imputer: BaseImputer = ImputerFactory.create_imputer(imputer_type, cpg_imputation)
            imputer.impute(dna_m)

            present_cpgs = self.cpgs[self.marker_name].values

        return present_cpgs, cpg_check

    def calculate(self, dna_m: pd.DataFrame, present_cpgs: np.ndarray, cpg_check: bool, pheno: Optional[pd.DataFrame], is_imputation: bool) -> Union[pd.DataFrame, pd.Series]:
        data: pd.DataFrame = dna_m[present_cpgs]

        if pheno is not None:
            pheno[self.name] = data.values
            return pheno
        else:
            return data
