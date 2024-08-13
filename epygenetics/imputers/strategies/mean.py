import pandas as pd

from epygenetics.imputers.base_imputer import BaseImputer


class MeanImputer(BaseImputer):
    """
    An imputer class that replaces missing values (NaNs) in a DNA methylation DataFrame
    with the mean of the non-missing values in the same row.
    """

    def impute(self, dna_m: pd.DataFrame) -> pd.DataFrame:
        """
        Imputes mean values for all NaN values in each row of the DataFrame.
        The mean is calculated from other non-NaN column values in the same row.

        Parameters:
            dna_m (pd.DataFrame): The input DataFrame with potential NaN values.

        Returns:
            pd.DataFrame: DataFrame with NaN values imputed using the row-wise mean.
        """
        # Iterate over each row in the DataFrame and impute NaN values with the row's mean
        for index, row in dna_m.iterrows():
            mean_value = row.mean()  # Calculate the mean of non-NaN values in the row
            dna_m.loc[index] = row.fillna(mean_value)  # Fill NaN values with the calculated mean

        return dna_m
