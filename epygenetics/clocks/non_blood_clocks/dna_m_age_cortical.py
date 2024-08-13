from typing import Optional, Union

import numpy as np
import pandas as pd

from epygenetics.clocks.base_clocks.regression_clock import RegressionClock
from epygenetics.clocks.type import ClockType
from epygenetics.utils.anti_trafo import anti_trafo


class DNAmAgeCorticalClock(RegressionClock):
    """
    A specific implementation of the `RegressionClock` for the DNAmAge Cortical clock.
    This clock predicts biological age specifically for cortical tissues based on DNA
    methylation data using predefined CpG sites and their associated regression coefficients.

    The CpG sites and regression coefficients are loaded from a CSV file during
    initialization. The calculation includes an anti-transformation step.
    """

    def __init__(self) -> None:
        """
        Initializes the DNAmAgeCorticalClock object by loading the necessary CpG sites
        and regression coefficients from a CSV file and setting the intercept
        for the regression model.
        """
        cpgs: Optional[pd.DataFrame] = pd.read_csv('data/CpGs/DNAmClockCortical_CpGs.csv')
        super().__init__(ClockType.DNAM_AGE_CORTICAL, 'CpGs', 'coef', 0.577682570446177, cpgs)

    def calculate(self,
                  dna_m: pd.DataFrame,
                  common_cpgs: np.ndarray,
                  cpg_check: bool,
                  pheno: Optional[pd.DataFrame],
                  is_imputation: bool
                  ) -> Union[pd.DataFrame, pd.Series]:
        """
        Calculates the predicted biological age using the DNAmAge Cortical clock model.

        If all required CpG sites are present or if imputation has been successfully
        performed, the biological age is calculated and then transformed using the
        anti-transformation function. The results are either added to the provided
        phenotype DataFrame or returned as a Series.

        Parameters:
            dna_m (pd.DataFrame): A DataFrame containing DNA methylation data.
            common_cpgs (np.ndarray): An array of CpG sites that are present in both
                                       the DNA methylation data and the clock's CpG list.
            cpg_check (bool): A boolean indicating whether all required CpG sites were found.
            pheno (Optional[pd.DataFrame]): A DataFrame containing phenotypic data. If provided,
                                            the calculated age is added to this DataFrame.
                                            Defaults to None.
            is_imputation (bool): Whether imputation was performed for missing CpG sites.

        Returns:
            Union[pd.DataFrame, pd.Series]: The predicted biological age either as a DataFrame
                                            if `pheno` is provided, with the age added to it,
                                            or as a Series if no `pheno` is provided.

        Raises:
            Exception: If the CpG check fails and imputation is not enabled or feasible.
        """
        if cpg_check or is_imputation:
            beta_values: pd.DataFrame = dna_m[common_cpgs]
            coefficients: pd.Series = self.cpgs.set_index(self.marker_name).loc[common_cpgs, self.coef_name]
            tt: np.ndarray = np.dot(beta_values, coefficients) + self.reg_coef
            dna_m_age_cortical: np.ndarray = anti_trafo(tt)

            if pheno is not None:
                pheno[self.name] = dna_m_age_cortical
                return pheno
            else:
                return pd.Series(dna_m_age_cortical, index=dna_m.index)

        else:
            raise Exception("CpG Check failed and imputation is not enabled or feasible.")
