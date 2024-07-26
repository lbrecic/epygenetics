import numpy as np

import pandas as pd
import pyreadr

from epygenetics.clocks.regression_clock import RegressionClock
from epygenetics.utils.anti_trafo import anti_trafo


class PEDBEClock(RegressionClock):
    def __init__(self):
        cpgs_dict = pyreadr.read_r('CpGs_data/PEDBE_CpGs.rda')
        cpgs = pd.DataFrame(cpgs_dict['PEDBE_CpGs'])
        super().__init__('PEDBE', cpgs, 'ID', 'Coef', -2.10)

    def calculate(self, common_cpgs, cpg_check, dna_m, pheno, imputation):
        if cpg_check or imputation:
            beta_values = dna_m[common_cpgs]
            coefficients = self.cpgs.set_index(self.marker_name).loc[common_cpgs, self.coef_name]
            tt = np.dot(beta_values, coefficients) - 2.10
            pedbe = anti_trafo(tt)

            if pheno is not None:
                pheno[self.name] = pedbe
                return pheno
            else:
                return pd.Series(pedbe, index=dna_m.index)

        else:
            raise Exception("CpG Check failed and imputation is not enabled or feasible.")
