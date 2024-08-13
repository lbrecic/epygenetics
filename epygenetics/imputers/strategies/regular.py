from typing import Optional

import pandas as pd

from epygenetics.imputers.base_imputer import BaseImputer


class RegularImputer(BaseImputer):
    """
    An imputer class that uses a predefined DataFrame of CpG imputation values to impute
    missing values in a DNA methylation DataFrame. The imputation is performed by replacing
    missing values with corresponding values from the CpG imputation DataFrame.
    """

    def __init__(self, cpg_imputation: Optional[pd.DataFrame]) -> None:
        """
        Initializes the RegularImputer with a DataFrame containing CpG imputation values.

        Parameters:
            cpg_imputation (Optional[pd.DataFrame]): A DataFrame containing imputation values
                                                     for missing CpGs. The first column should
                                                     contain CpG identifiers, and the second column
                                                     should contain the corresponding imputation values.
        """
        self.cpg_imputation: Optional[pd.DataFrame] = cpg_imputation

    def impute(self, dna_m: pd.DataFrame) -> pd.DataFrame:
        """
        Imputes missing values in the DNA methylation DataFrame using the provided CpG imputation values.

        Parameters:
            dna_m (pd.DataFrame): The input DNA methylation DataFrame with potential missing values.

        Returns:
            pd.DataFrame: A DataFrame with missing CpG values imputed using the provided CpG imputation data.

        Raises:
            ValueError: If the input dna_m or cpg_imputation is not a pandas DataFrame.
        """
        if not isinstance(dna_m, pd.DataFrame) or not isinstance(self.cpg_imputation, pd.DataFrame):
            raise ValueError("Inputs must be a pandas DataFrame")

        for cpg in dna_m.columns:
            if dna_m[cpg].isna().all():
                headers = self.cpg_imputation.columns.tolist()
                dna_m[cpg] = self.cpg_imputation[self.cpg_imputation[headers[0]] == cpg][headers[1]].values[0]

        return dna_m
