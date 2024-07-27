import pandas as pd
import numpy as np

from epygenetics.clocks.clock import Clock


class EpiTOC2Clock(Clock):
    def __init__(self, approximated=False, weights='delta', bias='beta0'):
        cpgs = pd.read_csv('../../../data/CpGs/EpiToc2_CpGs.csv')
        super().__init__('EpiTOC2', cpgs, 'EpiToc2_CpGs')
        self.approximated = approximated
        self.weights = weights
        self.bias = bias

    def check_cpgs(self, dna_m, cpg_imputation, imputation):
        common_cpgs = np.intersect1d(self.cpgs.index, dna_m.columns)
        cpg_check = len(self.cpgs.index) == len(common_cpgs)

        if not cpg_check and imputation:
            if cpg_imputation is None:
                raise ValueError("Necessary CpG is missing and no imputation data provided!")

            # Impute missing CpG values
            print(f"Imputation of missing CpG Values occurred for {self.name}")
            for cpg in self.cpgs.index:
                if cpg not in dna_m.columns:
                    mean_val = cpg_imputation.get(cpg, None)
                    if mean_val is None:
                        raise ValueError(f"No imputation value provided for missing CpG: {cpg}")
                    dna_m[cpg] = mean_val
            common_cpgs = self.cpgs.index

        return common_cpgs, cpg_check

    def calculate(self, common_cpgs, cpg_check, dna_m, pheno, imputation):
        if cpg_check or imputation:
            beta_values = dna_m[common_cpgs]
            weights = self.cpgs.loc[common_cpgs, self.weights]
            biases = self.cpgs.loc[common_cpgs, self.bias]

            # Calculate TNSC.v
            tnsc_v = 2 * np.mean(np.dot(beta_values - biases, 1 / (weights * (1 - weights))), axis=1)
            # Calculate TNSC2.v if approximated
            if self.approximated:
                tnsc_v = 2 * np.mean(np.dot(beta_values, 1 / weights), axis=1)

            if pheno is not None:
                pheno[self.name] = tnsc_v
                return pheno
            else:
                return pd.Series(tnsc_v, index=dna_m.index)

        else:
            raise Exception("CpG Check failed and imputation is not enabled or feasible.")
