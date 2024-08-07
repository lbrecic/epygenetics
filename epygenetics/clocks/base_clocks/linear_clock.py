from typing import Optional, Tuple, Union

import numpy as np
import pandas as pd

from epygenetics.clocks.base_clocks.clock import Clock


class LinearClock(Clock):
    def check_cpgs(self, dna_m: pd.DataFrame, cpg_imputation: Optional[pd.DataFrame], is_imputation: bool) -> Tuple[np.ndarray, bool]:
        present_cpgs: np.ndarray = np.intersect1d(self.cpgs, dna_m.columns)
        cpg_check: bool = len(self.cpgs) == len(present_cpgs)

        if not cpg_check and is_imputation:
            if cpg_imputation is None:
                raise ValueError("Necessary CpG is missing and no imputation data provided!")

            # Impute missing CpG values
            print(f"Imputation of missing CpG Values occurred for {self.name}")
            for cpg in self.cpgs:
                if cpg not in dna_m.columns:
                    headers = cpg_imputation.columns.tolist()
                    mean_val: Optional[float] = cpg_imputation[cpg_imputation[headers[0]] == cpg][headers[1]].values[0]
                    if mean_val is None:
                        raise ValueError(f"No imputation value provided for missing CpG: {cpg}")
                    dna_m[cpg] = mean_val
            present_cpgs = self.cpgs[self.marker_name].values

        return present_cpgs, cpg_check

    def calculate(self, present_cpgs: np.ndarray, cpg_check: bool, dna_m: pd.DataFrame, pheno: Optional[pd.DataFrame], is_imputation: bool) -> Union[pd.DataFrame, pd.Series]:
        data: pd.DataFrame = dna_m[present_cpgs]

        if pheno is not None:
            pheno[self.name] = data.values
            return pheno
        else:
            return data
