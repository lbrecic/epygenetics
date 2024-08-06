import pandas as pd


def median_impute(df: pd.DataFrame) -> pd.DataFrame:
    """
    This function imputes missing values in a pandas DataFrame using the median of each column.

    Parameters:
    df (pd.DataFrame): The input DataFrame with missing values.

    Returns:
    pd.DataFrame: A DataFrame with missing values imputed using the median.
    """
    # Ensure the input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame")

    # Perform median imputation
    return df.apply(lambda x: x.fillna(x.median()), axis=0)
