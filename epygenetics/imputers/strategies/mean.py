import pandas as pd

from epygenetics.imputers.base_imputer import BaseImputer


class MeanImputer(BaseImputer):
    def impute(self, dna_m: pd.DataFrame) -> pd.DataFrame:
        """
        This function imputes mean values for all np.NaN values in each row.
        The mean is calculated from other column values in the same row that are not np.NaN.

        Parameters:
        df (pd.DataFrame): The input DataFrame with potential np.NaN values.

        Returns:
        pd.DataFrame: DataFrame with np.NaN values imputed with row-wise mean.
        """
        # Calculate the mean for each row and replace NaN values with the mean
        for index, row in dna_m.iterrows():
            mean_value = row.mean()  # Calculate the mean of non-NaN values in the row
            dna_m.loc[index] = row.fillna(mean_value)  # Fill NaN values with the calculated mean

        return dna_m
