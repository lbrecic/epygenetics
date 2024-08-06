import pandas as pd
from sklearn.impute import KNNImputer


def knn_impute(df: pd.DataFrame, n_neighbors: int = 5) -> pd.DataFrame:
    """
    This function imputes missing values in a pandas DataFrame using the K-Nearest Neighbors algorithm.

    Parameters:
    df (pd.DataFrame): The input DataFrame with missing values.
    n_neighbors (int): Number of neighboring samples to use for imputation (default is 5).

    Returns:
    pd.DataFrame: A DataFrame with missing values imputed using the KNN algorithm.
    """
    # Ensure the input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame")

    # Perform KNN imputation
    knn_imputer = KNNImputer(n_neighbors=n_neighbors)
    return pd.DataFrame(knn_imputer.fit_transform(df), columns=df.columns)
