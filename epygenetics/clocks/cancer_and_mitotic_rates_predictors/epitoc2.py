from typing import Optional, Tuple, Union

import numpy as np
import pandas as pd

from epygenetics.clocks.base_clocks.clock import Clock


class EpiTOC2Clock(Clock):
    def __init__(self, approximated: bool = False, weights: str = 'delta', bias: str = 'beta0') -> None:
        cpgs: Optional[pd.DataFrame] = pd.read_csv('data/CpGs/EpiToc2_CpGs.csv')
        super().__init__('EpiTOC2', 'EpiToc2_CpGs', cpgs)
        self.approximated: bool = approximated
        self.weights: str = weights
        self.bias: str = bias

    def check_cpgs(self, dna_m: pd.DataFrame, cpg_imputation: Optional[pd.DataFrame], imputation: bool) -> Tuple[np.ndarray, bool]:
        common_cpgs: np.ndarray = np.intersect1d(self.cpgs[self.weights], dna_m.columns)
        cpg_check: bool = len(self.cpgs[self.weights]) == len(common_cpgs)

        if not cpg_check and imputation:
            if cpg_imputation is None:
                raise ValueError("Necessary CpG is missing and no imputation data provided!")

            # Impute missing CpG values
            print(f"Imputation of missing CpG Values occurred for {self.name}")
            for cpg in self.cpgs[self.weights]:
                if cpg not in dna_m.columns:
                    mean_val: Optional[float] = cpg_imputation.get(cpg, None)
                    if mean_val is None:
                        raise ValueError(f"No imputation value provided for missing CpG: {cpg}")
                    dna_m[cpg] = mean_val
            common_cpgs = self.cpgs[self.weights].values

        return common_cpgs, cpg_check

    def calculate(self, common_cpgs: np.ndarray, cpg_check: bool, dna_m: pd.DataFrame, pheno: Optional[pd.DataFrame], imputation: bool) -> Union[pd.DataFrame, pd.Series]:
        if cpg_check or imputation:
            beta_values: pd.DataFrame = dna_m[common_cpgs]
            weights: pd.Series = self.cpgs.loc[common_cpgs, self.weights]
            biases: pd.Series = self.cpgs.loc[common_cpgs, self.bias]

            # Calculate TNSC.v
            tnsc_v: np.ndarray = 2 * np.mean(np.dot(beta_values - biases, 1 / (weights * (1 - weights))), axis=1)
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
