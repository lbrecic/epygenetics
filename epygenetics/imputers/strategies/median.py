import pandas as pd

from epygenetics.imputers.base_imputer import BaseImputer


class MedianImputer(BaseImputer):
    """
    An imputer class that replaces missing values (NaNs) in a DNA methylation DataFrame
    with the median of the non-missing values in the same row.
    """

    def impute(self, dna_m: pd.DataFrame) -> pd.DataFrame:
        """
        Imputes median values for all NaN values in each row of the DataFrame.
        The median is calculated from other non-NaN column values in the same row.

        Parameters:
            dna_m (pd.DataFrame): The input DataFrame with potential NaN values.

        Returns:
            pd.DataFrame: DataFrame with NaN values imputed using the row-wise median.
        """
        # Iterate over each row in the DataFrame and impute NaN values with the row's median
        for index, row in dna_m.iterrows():
            median_value = row.median()  # Calculate the median of non-NaN values in the row
            dna_m.loc[index] = row.fillna(median_value)  # Fill NaN values with the calculated median

        return dna_m
