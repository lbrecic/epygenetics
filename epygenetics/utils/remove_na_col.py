import pandas as pd


def remove_na_col(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove columns from a DataFrame that contain only NA values.

    Parameters:
    df : DataFrame
        A pandas DataFrame of CpG Betas with CpGs of all NA values.

    Returns:
    DataFrame
        A DataFrame with NA columns removed.
    """
    # Remove columns where all values are NaN
    df_cleaned: pd.DataFrame = df.loc[:, ~df.isna().all()]
    return df_cleaned

# Example usage
# df = pd.read_csv('exampleBetas.csv')  # Example input DataFrame
# result = remove_na_col(df)
