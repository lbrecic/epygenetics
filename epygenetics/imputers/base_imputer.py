from abc import ABC, abstractmethod

import pandas as pd


class BaseImputer(ABC):
    """
    An abstract base class for imputers used to handle missing data in DNA methylation datasets.
    Subclasses must implement the `impute` method, which defines the strategy for imputing missing values.
    """

    @abstractmethod
    def impute(self, dna_m: pd.DataFrame) -> pd.DataFrame:
        """
        Imputes missing values in the provided DNA methylation DataFrame.

        Parameters:
            dna_m (pd.DataFrame): A DataFrame containing DNA methylation data with possible missing values.

        Returns:
            pd.DataFrame: A DataFrame with missing values imputed according to the specific imputation strategy.
        """
        pass
