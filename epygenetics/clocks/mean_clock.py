import numpy as np
import pandas as pd
from .clock import Clock


class MeanClock(Clock):
    def check_cpgs(self, dna_m, cpg_imputation, imputation):
        present_cpgs = np.intersect1d(self.cpgs, dna_m.columns)
        cpg_check = len(self.cpgs) == len(present_cpgs)

        if not cpg_check and imputation:
            if cpg_imputation is None:
                raise ValueError("Necessary CpG is missing and no imputation data provided!")

            # Impute missing CpG values
            print(f"Imputation of missing CpG Values occurred for {self.name}")
            for cpg in self.cpgs:
                if cpg not in dna_m.columns:
                    mean_val = cpg_imputation.get(cpg)
                    if mean_val is None:
                        raise ValueError(f"No imputation value provided for missing CpG: {cpg}")
                    dna_m[cpg] = mean_val
            present_cpgs = self.cpgs

        return present_cpgs, cpg_check

    def calculate(self, common_cpgs, cpg_check, dna_m, pheno, imputation):
        if cpg_check or imputation:
            map_idx = dna_m.columns.get_indexer(common_cpgs)
            mean_v = dna_m.iloc[:, map_idx].mean(axis=1, skipna=True)

            if pheno is not None:
                pheno[self.name] = mean_v
                return pheno
            else:
                return pd.Series(mean_v, index=dna_m.index)

        else:
            raise Exception("CpG Check failed and imputation is not enabled or feasible.")
