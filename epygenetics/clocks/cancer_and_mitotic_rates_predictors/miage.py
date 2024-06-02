import pandas as pd
import pyreadr

from epygenetics.clocks.regression_clock import RegressionClock
from epygenetics.utils.mi_age_mitotic_age import miage_mitotic_age


class MiAgeClock(RegressionClock):
    def __init__(self, *miage_params):
        cpgs_dict = pyreadr.read_r('CpGs_data/MiAge_CpGs.rda')
        cpgs = pd.DataFrame(cpgs_dict['MiAge_CpGs'])
        super().__init__('MiAge', cpgs, 'CpGs', 'Age-hyper/Age-hypo', 0)
        self.miage_params = miage_params

    def calculate(self, common_cpgs, cpg_check, dna_m, pheno, imputation):
        if cpg_check or imputation:
            beta_values = dna_m[common_cpgs]
            transposed_data = beta_values.T  # Transpose data to match expected input format
            miage = miage_mitotic_age(transposed_data, *self.miage_params)

            if pheno is not None:
                pheno[self.name] = miage
                return pheno
            else:
                return pd.Series(miage, index=dna_m.index)

        else:
            raise Exception("CpG Check failed and imputation is not enabled or feasible.")
