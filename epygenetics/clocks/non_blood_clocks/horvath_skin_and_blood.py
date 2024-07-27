import pandas as pd
import numpy as np

from epygenetics.clocks.regression_clock import RegressionClock
from epygenetics.utils.anti_trafo import anti_trafo


class HorvathSkinAndBloodClock(RegressionClock):
    def __init__(self):
        cpgs = pd.read_csv('../../CpGs/Horvath2_CpGs.csv')
        super().__init__('Horvath2', cpgs, 'ID', 'Coef', -0.447119319)

    def calculate(self, common_cpgs, cpg_check, dna_m, pheno, imputation):
        if cpg_check or imputation:
            beta_values = dna_m[common_cpgs]
            coefficients = self.cpgs.set_index(self.marker_name).loc[common_cpgs, self.coef_name]
            tt = np.dot(beta_values, coefficients) + self.reg_coef
            dna_m_age_cortical = anti_trafo(tt)

            if pheno is not None:
                pheno[self.name] = dna_m_age_cortical
                return pheno
            else:
                return pd.Series(dna_m_age_cortical, index=dna_m.index)

        else:
            raise Exception("CpG Check failed and imputation is not enabled or feasible.")
