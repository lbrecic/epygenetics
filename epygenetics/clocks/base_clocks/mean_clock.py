from typing import Optional, Tuple, Union

import numpy as np
import pandas as pd

from epygenetics.clocks.base_clocks.clock import Clock


class MeanClock(Clock):
    def check_cpgs(self, dna_m: pd.DataFrame, cpg_imputation: Optional[pd.DataFrame], is_imputation: bool) -> Tuple[np.ndarray, bool]:
        present_cpgs: np.ndarray = np.intersect1d(self.cpgs[self.marker_name], dna_m.columns)
        cpg_check: bool = len(self.cpgs[self.marker_name]) == len(present_cpgs)

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

    def calculate(self, common_cpgs: np.ndarray, cpg_check: bool, dna_m: pd.DataFrame, pheno: Optional[pd.DataFrame], is_imputation: bool) -> Union[pd.DataFrame, pd.Series]:
        if cpg_check or is_imputation:
            map_idx = dna_m.columns.get_indexer(common_cpgs)
            mean_v = dna_m.iloc[:, map_idx].mean(axis=1, skipna=True)

            if pheno is not None:
                pheno[self.name] = mean_v
                return pheno
            else:
                return pd.Series(mean_v, index=dna_m.index)

        else:
            raise Exception("CpG Check failed and imputation is not enabled or feasible.")
