import pandas as pd
import numpy as np
import pyreadr

from epygenetics.clocks.regression_clock import RegressionClock


class LeeControlClock(RegressionClock):
    def __init__(self):
        cpgs_dict = pyreadr.read_r('../../../CpGs_data/`LeeRobust`_CpGs.rda')
        cpgs = pd.DataFrame(cpgs_dict['LeeRobust_CpGs'])
        super().__init__('LeeRobust', cpgs, 'CpG', 'coef', 24.99772)

    def check_cpgs(self, dna_m, cpg_imputation, imputation):
        common_cpgs = self.cpgs[self.marker_name].isin(dna_m.columns)
        cpg_check = common_cpgs.all()

        if not cpg_check and imputation:
            if CpGImputation is None:
                raise ValueError("Necessary CpG is missing and no imputation data provided!")

            # Impute missing CpG values
            for cpg in LeeRobust_CpGs.loc[~common_cpgs, 'CpG']:
                if cpg in CpGImputation:
                    DNAm[cpg] = DNAm.get(cpg, CpGImputation[cpg])
                else:
                    raise ValueError(f"No imputation value provided for missing CpG: {cpg}")
            common_cpgs = LeeRobust_CpGs['CpG'].isin(DNAm.columns)
            cpg_check = common_cpgs.all()


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
