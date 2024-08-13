import pandas as pd


def remove_na_col(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove columns from a DataFrame that contain only NA values.

    Parameters:
        df (pd.DataFrame): A pandas DataFrame containing CpG Betas, potentially with columns of all NA values.

    Returns:
        pd.DataFrame: A DataFrame with columns containing only NA values removed.
    """
    # Remove columns where all values are NaN
    df_cleaned: pd.DataFrame = df.loc[:, ~df.isna().all()]
    return df_cleaned
