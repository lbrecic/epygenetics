import numpy as np
from .clock import Clock


class LinearClock(Clock):
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

    def calculate(self, present_cpgs, cpg_check, dna_m, pheno, imputation):
        data = dna_m[present_cpgs]

        if pheno is not None:
            pheno[self.name] = data.values
            return pheno
        else:
            return data
