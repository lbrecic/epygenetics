import pandas as pd
from sklearn.experimental import enable_iterative_imputer  # noqa
from sklearn.impute import IterativeImputer


def mice_impute(df: pd.DataFrame) -> pd.DataFrame:
    """
    This function imputes missing values in a pandas DataFrame using the MICE algorithm.

    Parameters:
    df (pd.DataFrame): The input DataFrame with missing values.

    Returns:
    pd.DataFrame: A DataFrame with missing values imputed using the MICE algorithm.
    """
    # Ensure the input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame")

    # Perform MICE imputation
    mice_imputer = IterativeImputer()
    return pd.DataFrame(mice_imputer.fit_transform(df), columns=df.columns)
