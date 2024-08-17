from typing import Optional, Tuple, Union

import numpy as np
import pandas as pd

from epygenetics.clocks.base_clocks.clock import Clock
from epygenetics.imputers.base_imputer import BaseImputer
from epygenetics.imputers.factory import ImputerFactory
from epygenetics.imputers.type import ImputerType


class LinearClock(Clock):
    """
    A concrete implementation of the `Clock` class that uses a linear model
    for predicting biological age or other phenotypic outcomes based on DNA
    methylation data.

    This class handles checking the presence of required CpG sites and, if
    necessary, imputes missing values using a specified imputer. It then
    performs the calculation based on the available or imputed CpG data.
    """

    def validate(self,
                 dna_m: pd.DataFrame,
                 is_imputation: bool = False,
                 imputer_type=ImputerType.REGULAR,
                 cpg_imputation: Optional[pd.DataFrame] = None
                 ) -> Tuple[np.ndarray, bool]:
        """
        Checks the presence of required CpG sites in the DNA methylation data and
        optionally imputes missing CpG values.

        Parameters:
            dna_m (pd.DataFrame): A DataFrame containing DNA methylation data.
            is_imputation (bool, optional): Whether to perform imputation for missing
                                            CpG sites. Defaults to False.
            imputer_type (ImputerType, optional): The type of imputer to use if
                                                  imputation is performed. Defaults to
                                                  ImputerType.REGULAR.
            cpg_imputation (Optional[pd.DataFrame], optional): A DataFrame containing
                                                               imputation data for CpG sites.
                                                               Defaults to None.

        Returns:
            Tuple[np.ndarray, bool]: A tuple containing an array of the CpG sites present
                                     in both the DNA methylation data and the clock's CpG list,
                                     and a boolean indicating whether all required CpG sites
                                     were found.

        Raises:
            ValueError: If the CpG sites have not been loaded into the clock.
        """
        if self.cpgs is None:
            raise ValueError("CpGs not loaded.")

        present_cpgs: np.ndarray = np.intersect1d(self.cpgs[self.marker_name], dna_m.columns)
        cpg_check: bool = len(self.cpgs[self.marker_name]) == len(present_cpgs)

        if not cpg_check and is_imputation:
            # Impute missing CpG values
            print(f"Imputation of missing CpG Values occurred for {self.name}")
            for cpg in self.cpgs[self.marker_name]:
                if cpg not in dna_m.columns:
                    dna_m[cpg] = np.nan

            imputer: BaseImputer = ImputerFactory.create_imputer(imputer_type, cpg_imputation)
            imputer.impute(dna_m)

            present_cpgs = self.cpgs[self.marker_name].values

        return present_cpgs, cpg_check

    def calculate(self, dna_m: pd.DataFrame, present_cpgs: np.ndarray, cpg_check: bool, pheno: Optional[pd.DataFrame],
                  is_imputation: bool) -> Union[pd.DataFrame, pd.Series]:
        """
        Calculates the biological age or other phenotypic outcomes based on the
        DNA methylation data.

        Parameters:
            dna_m (pd.DataFrame): A DataFrame containing DNA methylation data.
            present_cpgs (np.ndarray): An array of CpG sites that are present in both
                                       the DNA methylation data and the clock's CpG list.
            cpg_check (bool): A boolean indicating whether all required CpG sites were found.
            pheno (Optional[pd.DataFrame]): A DataFrame containing phenotypic data. If provided,
                                            the calculated values are added to this DataFrame.
                                            Defaults to None.
            is_imputation (bool): Whether imputation was performed for missing CpG sites.

        Returns:
            Union[pd.DataFrame, pd.Series]: The result of the calculation, either as a DataFrame
                                            if `pheno` is provided, with the calculated values
                                            added to it, or as a Series if no `pheno` is provided.
        """
        data: pd.DataFrame = dna_m[present_cpgs]

        if pheno is not None:
            pheno[self.name] = data.values
            return pheno
        else:
            return data
