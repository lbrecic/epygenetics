from typing import Any, Optional, Tuple, Union

import numpy as np
import pandas as pd

from epygenetics.clocks.base_clocks.regression_clock import RegressionClock
from epygenetics.clocks.type import ClockType
from epygenetics.store import AbstractDataStore
from epygenetics.store.strategies import CSVDataStore
from epygenetics.utils.mi_age_mitotic_age import miage_mitotic_age


class MiAgeClock(RegressionClock):
    """
    A specific implementation of the `RegressionClock` for the MiAge clock.
    This clock predicts mitotic age based on DNA methylation data using predefined
    CpG sites and their associated regression coefficients.

    The CpG sites and regression coefficients are loaded from a CSV file during
    initialization, and the MiAge calculation utilizes additional parameters
    passed during initialization.
    """

    def __init__(self, *miage_params: Any) -> None:
        """
        Initializes the MiAgeClock object by loading the necessary CpG sites
        and regression coefficients from a CSV file and storing additional
        parameters for the MiAge calculation.

        Parameters:
            miage_params (Any): Additional parameters required for the
                                MiAge calculation.
        """
        store: AbstractDataStore = CSVDataStore('data/CpGs')
        cpgs: Optional[pd.DataFrame] = store.retrieve_methylation_data(ClockType.MIAGE)
        super().__init__(ClockType.MIAGE, 'CpGs', 'Age-hyper/Age-hypo', 0, cpgs)
        self.miage_params: Tuple[Any, ...] = miage_params

    def calculate(self,
                  dna_m: pd.DataFrame,
                  common_cpgs: np.ndarray,
                  cpg_check: bool,
                  pheno: Optional[pd.DataFrame],
                  is_imputation: bool
                  ) -> Union[pd.DataFrame, pd.Series]:
        """
        Calculates the mitotic age (MiAge) based on the specified CpG sites and
        their corresponding regression coefficients.

        If all required CpG sites are present or if imputation has been successfully
        performed, the MiAge is calculated. The results are either added to the provided
        phenotype DataFrame or returned as a Series.

        Parameters:
            dna_m (pd.DataFrame): A DataFrame containing DNA methylation data.
            common_cpgs (np.ndarray): An array of CpG sites that are present in both
                                       the DNA methylation data and the clock's CpG list.
            cpg_check (bool): A boolean indicating whether all required CpG sites were found.
            pheno (Optional[pd.DataFrame]): A DataFrame containing phenotypic data. If provided,
                                            the calculated MiAge is added to this DataFrame.
                                            Defaults to None.
            is_imputation (bool): Whether imputation was performed for missing CpG sites.

        Returns:
            Union[pd.DataFrame, pd.Series]: The calculated MiAge either as a DataFrame
                                            if `pheno` is provided, with the MiAge added to it,
                                            or as a Series if no `pheno` is provided.

        Raises:
            Exception: If the CpG check fails and imputation is not enabled or feasible.
        """
        if cpg_check or is_imputation:
            beta_values: pd.DataFrame = dna_m[common_cpgs]
            transposed_data: pd.DataFrame = beta_values.T  # Transpose data to match expected input format
            miage: np.ndarray = miage_mitotic_age(transposed_data, *self.miage_params)

            if pheno is not None:
                pheno[self.name] = miage
                return pheno
            else:
                return pd.Series(miage, index=dna_m.index)

        else:
            raise Exception("CpG Check failed and imputation is not enabled or feasible.")
