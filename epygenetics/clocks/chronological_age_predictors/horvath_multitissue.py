import pandas as pd
import numpy as np
import pyreadr

from masters_thesis.epygenetics.clocks.regression_clock import RegressionClock
from masters_thesis.epygenetics.utils.anti_trafo import anti_trafo

class HorvathMultitissueClock(RegressionClock):
    def __init__(self):
        cpgs_dict = pyreadr.read_r('CpGs_data/Horvath1_CpGs.rda')
        cpgs = pd.DataFrame(cpgs_dict['Horvath1_CpGs'])
        super().__init__('Horvath1', cpgs, 'CpGmarker', 'CoefficientTraining', 0.696)

    def calculate(self, common_cpgs, cpg_check, dna_m, pheno, imputation):
        if cpg_check or imputation:
            beta_values = dna_m[common_cpgs]
            coefficients = self.cpgs.set_index(self.marker_name).loc[common_cpgs, self.coef_name]
            tt = np.dot(beta_values, coefficients) + self.reg_coef
            horvath1 = anti_trafo(tt)

            if pheno is not None:
                pheno[self.name] = horvath1
                return pheno
            else:
                return pd.Series(horvath1, index=dna_m.index)

        else:
            raise Exception("CpG Check failed and imputation is not enabled or feasible.")