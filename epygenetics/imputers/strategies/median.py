import pandas as pd

from epygenetics.imputers.base_imputer import BaseImputer


class MedianImputer(BaseImputer):
    def impute(self, dna_m: pd.DataFrame) -> pd.DataFrame:
        """
        This function imputers missing values in a pandas DataFrame using the median of each column.

        Parameters:
        df (pd.DataFrame): The input DataFrame with missing values.

        Returns:
        pd.DataFrame: A DataFrame with missing values imputed using the median.
        """
        # Ensure the input is a DataFrame
        if not isinstance(dna_m, pd.DataFrame):
            raise ValueError("Input must be a pandas DataFrame")

        # Perform median imputation
        return dna_m.apply(lambda x: x.fillna(x.median()), axis=0)
