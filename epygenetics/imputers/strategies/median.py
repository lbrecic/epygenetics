import pandas as pd

from epygenetics.imputers.base_imputer import BaseImputer


class MedianImputer(BaseImputer):
    def impute(self, dna_m: pd.DataFrame) -> pd.DataFrame:
        """
        This function imputes median values for all np.NaN values in each row.
        The median is calculated from other column values in the same row that are not np.NaN.

        Parameters:
        df (pd.DataFrame): The input DataFrame with potential np.NaN values.

        Returns:
        pd.DataFrame: DataFrame with np.NaN values imputed with row-wise median.
        """
        # Calculate the median for each row and replace NaN values with the median
        for index, row in dna_m.iterrows():
            median_value = row.median()  # Calculate the median of non-NaN values in the row
            dna_m.loc[index] = row.fillna(median_value)  # Fill NaN values with the calculated median

        return dna_m
