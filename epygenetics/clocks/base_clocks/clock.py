from abc import ABC, abstractmethod
from typing import Any, Optional, Tuple, Union

import numpy as np
import pandas as pd

from epygenetics.imputers.type import ImputerType


class Clock(ABC):
    """
    An abstract base class for implementing epigenetic clocks. This class provides
    a framework for loading CpG data, checking the consistency of CpG sites between
    datasets, and calculating biological age or other phenotypic outcomes based on
    DNA methylation data.

    Attributes:
        name (str): The name of the epigenetic clock.
        marker_name (str): The name of the marker (e.g., biological age) that this clock predicts.
        cpgs (Optional[pd.DataFrame]): A DataFrame containing CpG sites relevant to the clock.
                                        This can be loaded from a CSV file or passed directly
                                        during initialization.
    """

    def __init__(self,
                 name: str,
                 marker_name: str,
                 cpgs: Optional[pd.DataFrame] = None
                 ) -> None:
        """
        Initializes the Clock object.

        Parameters:
            name (str): The name of the epigenetic clock.
            marker_name (str): The name of the marker being predicted by this clock.
            cpgs (Optional[pd.DataFrame]): A DataFrame containing CpG sites. If not provided,
                                           it can be loaded later using load_cpgs_from_csv.
        """
        self.name: str = name
        self.marker_name: str = marker_name
        self.cpgs: Optional[pd.DataFrame] = cpgs

    def load_cpgs_from_csv(self, path: str) -> None:
        """
        Loads CpG data from a CSV file and stores it in the cpgs attribute.

        Parameters:
            path (str): The file path to the CSV containing CpG site data.
        """
        self.cpgs = pd.read_csv(path)

    @abstractmethod
    def validate(self, dna_m: pd.DataFrame,
                 is_imputation: bool = False,
                 imputer_type=ImputerType.REGULAR,
                 cpg_imputation: Optional[pd.DataFrame] = None
                 ) -> Tuple[np.ndarray, bool]:
        """
        Checks the consistency and availability of CpG sites between the input DNA methylation
        data and the required CpG sites for the clock. This is an abstract method that must be
        implemented by subclasses.

        Parameters:
            dna_m (pd.DataFrame): A DataFrame containing DNA methylation data.
            is_imputation (bool, optional): Whether to perform imputation for missing CpG sites.
                                            Defaults to False.
            imputer_type (ImputerType, optional): The type of imputer to use if imputation is performed.
                                                  Defaults to ImputerType.REGULAR.
            cpg_imputation (Optional[pd.DataFrame], optional): A DataFrame containing imputation data
                                                               for CpG sites. Defaults to None.

        Returns:
            Tuple[np.ndarray, bool]: A tuple containing an array of common CpG sites and a boolean
                                     indicating if the check was successful.
        """
        pass

    @abstractmethod
    def calculate(self, dna_m: pd.DataFrame,
                  common_cpgs: np.ndarray,
                  cpg_check: Any,
                  pheno: Optional[pd.DataFrame],
                  is_imputation: bool
                  ) -> Union[pd.DataFrame, pd.Series]:
        """
        Performs the calculation of the predicted biological age or other phenotypic outcomes
        based on the DNA methylation data. This is an abstract method that must be implemented
        by subclasses.

        Parameters:
            dna_m (pd.DataFrame): A DataFrame containing DNA methylation data.
            common_cpgs (np.ndarray): An array of CpG sites common between the input data and
                                      the required CpG sites for the clock.
            cpg_check (Any): The result of the CpG check, typically a flag or additional data.
            pheno (Optional[pd.DataFrame]): A DataFrame containing phenotypic data, if relevant
                                            for the calculation. Defaults to None.
            is_imputation (bool): Whether imputation was performed for missing CpG sites.

        Returns:
            Union[pd.DataFrame, pd.Series]: The result of the calculation, either as a DataFrame
                                            or a Series, depending on the implementation.
        """
        pass

    def execute(self,
                dna_m: pd.DataFrame,
                pheno: Optional[pd.DataFrame] = None,
                is_imputation: bool = False,
                imputation_type=ImputerType.REGULAR,
                cpg_imputation: Optional[pd.DataFrame] = None
                ) -> None:
        """
        Executes the full process of validating CpG sites and calculating the predicted
        biological age or other outcomes. This method uses the check_cpgs and calculate
        methods defined in the subclasses.

        Parameters:
            dna_m (pd.DataFrame): A DataFrame containing DNA methylation data.
            pheno (Optional[pd.DataFrame], optional): A DataFrame containing phenotypic data.
                                                      Defaults to None.
            is_imputation (bool, optional): Whether to perform imputation for missing CpG sites.
                                            Defaults to False.
            imputation_type (ImputerType, optional): The type of imputer to use if imputation is performed.
                                                     Defaults to ImputerType.REGULAR.
            cpg_imputation (Optional[pd.DataFrame], optional): A DataFrame containing imputation data
                                                               for CpG sites. Defaults to None.
        """
        cpgs, cpg_check = self.validate(dna_m, is_imputation, imputation_type, cpg_imputation)
        result = self.calculate(dna_m, cpgs, cpg_check, pheno, is_imputation)
        print(result)
