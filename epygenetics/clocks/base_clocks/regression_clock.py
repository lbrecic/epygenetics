import numpy as np
import pandas as pd

from epygenetics.clocks.base_clocks.clock import Clock


class RegressionClock(Clock):
    def __init__(self, name, cpgs, marker_name, coef_name, reg_coef):
        super().__init__(name, cpgs, marker_name)
        self.coef_name = coef_name
        self.reg_coef = reg_coef

    def check_cpgs(self, dna_m, cpg_imputation, imputation):
        common_cpgs = np.intersect1d(self.cpgs[self.marker_name], dna_m.columns)
        cpg_check = len(self.cpgs[self.marker_name]) == len(common_cpgs)

        if not cpg_check and imputation:
            if cpg_imputation is None:
                raise ValueError("Necessary CpG is missing and no imputation data provided!")

            # Impute missing CpG values
            print(f"Imputation of missing CpG Values occurred for {self.name}")
            for cpg in self.cpgs[self.marker_name]:
                if cpg not in dna_m.columns:
                    mean_val = cpg_imputation.get(cpg, None)
                    if mean_val is None:
                        raise ValueError(f"No imputation value provided for missing CpG: {cpg}")
                    dna_m[cpg] = mean_val
            common_cpgs = self.cpgs[self.marker_name]

        return common_cpgs, cpg_check

    def calculate(self, common_cpgs, cpg_check, dna_m, pheno, imputation):
        if cpg_check or imputation:
            beta_values = dna_m[common_cpgs]
            coefficients = self.cpgs.set_index(self.marker_name).loc[common_cpgs, self.coef_name]
            tt = np.dot(beta_values, coefficients) + self.reg_coef

            if pheno is not None:
                pheno[self.name] = tt
                return pheno
            else:
                return pd.Series(tt, index=dna_m.index)

        else:
            raise Exception("CpG Check failed and imputation is not enabled or feasible.")
