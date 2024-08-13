from typing import Optional, Tuple, Union

import numpy as np
import pandas as pd

from epygenetics.clocks.base_clocks.clock import Clock
from epygenetics.imputers.base_imputer import BaseImputer
from epygenetics.imputers.factory import ImputerFactory
from epygenetics.imputers.type import ImputerType


class RegressionClock(Clock):
    """
    A concrete implementation of the `Clock` class that uses a linear regression model
    to predict biological age or other phenotypic outcomes based on DNA methylation data.

    This class checks for the presence of required CpG sites, imputes missing values if
    necessary, and calculates the predicted outcome using a set of regression coefficients.
    """

    def __init__(self,
                 name: str,
                 marker_name: str,
                 coef_name: str,
                 reg_coef: float,
                 cpgs: Optional[pd.DataFrame] = None
                 ) -> None:
        """
        Initializes the RegressionClock object.

        Parameters:
            name (str): The name of the epigenetic clock.
            marker_name (str): The name of the marker being predicted by this clock.
            coef_name (str): The name of the column in the CpG DataFrame that contains
                             the regression coefficients.
            reg_coef (float): The intercept term for the regression model.
            cpgs (Optional[pd.DataFrame]): A DataFrame containing CpG sites and their corresponding
                                           regression coefficients. If not provided, it can be
                                           loaded later using load_cpgs_from_csv.
        """
        super().__init__(name, marker_name, cpgs)
        self.coef_name: str = coef_name
        self.reg_coef: float = reg_coef

    def check_cpgs(self,
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

        common_cpgs: np.ndarray = np.intersect1d(self.cpgs[self.marker_name], dna_m.columns)
        cpg_check: bool = len(self.cpgs[self.marker_name]) == len(common_cpgs)

        if not cpg_check and is_imputation:
            # Impute missing CpG values
            print(f"Imputation of missing CpG Values occurred for {self.name}")
            for cpg in self.cpgs[self.marker_name]:
                if cpg not in dna_m.columns:
                    dna_m[cpg] = np.nan

            imputer: BaseImputer = ImputerFactory.create_imputer(imputer_type, cpg_imputation)
            imputer.impute(dna_m)

            common_cpgs = self.cpgs[self.marker_name].values

        return common_cpgs, cpg_check

    def calculate(self,
                  dna_m: pd.DataFrame,
                  common_cpgs: np.ndarray,
                  cpg_check: bool,
                  pheno: Optional[pd.DataFrame],
                  is_imputation: bool
                  ) -> Union[pd.DataFrame, pd.Series]:
        """
        Calculates the predicted outcome using a linear regression model based on the
        specified CpG sites and their corresponding regression coefficients.

        If all required CpG sites are present or if imputation has been successfully
        performed, the predicted outcome is calculated. The results are either added
        to the provided phenotype DataFrame or returned as a Series.

        Parameters:
            dna_m (pd.DataFrame): A DataFrame containing DNA methylation data.
            common_cpgs (np.ndarray): An array of CpG sites that are present in both
                                       the DNA methylation data and the clock's CpG list.
            cpg_check (bool): A boolean indicating whether all required CpG sites were found.
            pheno (Optional[pd.DataFrame]): A DataFrame containing phenotypic data. If provided,
                                            the calculated values are added to this DataFrame.
                                            Defaults to None.
            is_imputation (bool): Whether imputation was performed for missing CpG sites.

        Returns:
            Union[pd.DataFrame, pd.Series]: The predicted outcome either as a DataFrame
                                            if `pheno` is provided, with the calculated values
                                            added to it, or as a Series if no `pheno` is provided.

        Raises:
            Exception: If the CpG check fails and imputation is not enabled or feasible.
        """
        if cpg_check or is_imputation:
            beta_values: pd.DataFrame = dna_m[common_cpgs]
            coefficients: pd.Series = self.cpgs.set_index(self.marker_name).loc[common_cpgs, self.coef_name]
            tt: np.ndarray = np.dot(beta_values, coefficients) + self.reg_coef

            if pheno is not None:
                pheno[self.name] = tt
                return pheno
            else:
                return pd.Series(tt, index=dna_m.index)

        else:
            raise Exception("CpG Check failed and imputation is not enabled or feasible.")
