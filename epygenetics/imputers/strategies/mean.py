import pandas as pd

from epygenetics.imputers.base_imputer import BaseImputer


class MeanImputer(BaseImputer):
    def impute(self, dna_m: pd.DataFrame) -> pd.DataFrame:
        """
            Perform mean imputation for singly missing CpGs in a dataframe of CpG Betas.

            Parameters:
            df : DataFrame
                A pandas DataFrame of CpG Betas with missing values.

            Returns:
            DataFrame
                Mean imputed DataFrame.
            """
        # Apply a lambda function to each column in the DataFrame
        # The lambda function checks for missing values and replaces them with the mean of the column
        return dna_m.apply(lambda x: x.fillna(x.mean()), axis=0)
