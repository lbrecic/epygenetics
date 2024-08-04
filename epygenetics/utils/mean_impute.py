import pandas as pd
from typing import Any


def mean_impute(df: pd.DataFrame) -> pd.DataFrame:
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
    return df.apply(lambda x: x.fillna(x.mean()), axis=0)

# Example usage:
# Assume df_cpgs is a DataFrame loaded with CpG beta values that possibly contain NaNs
# df_imputed = mean_impute(df_cpgs)
