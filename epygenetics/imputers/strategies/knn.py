import pandas as pd
from sklearn.impute import KNNImputer as KNN

from epygenetics.imputers.base_imputer import BaseImputer


class KNNImputer(BaseImputer):
    def __init__(self, n_neighbors: int = 5) -> None:
        self.n_neighbors: int = n_neighbors

    def impute(self, dna_m: pd.DataFrame) -> pd.DataFrame:
        """
            This function imputers missing values in a pandas DataFrame using the K-Nearest Neighbors algorithm.

            Parameters:
            df (pd.DataFrame): The input DataFrame with missing values.
            n_neighbors (int): Number of neighboring samples to use for imputation (default is 5).

            Returns:
            pd.DataFrame: A DataFrame with missing values imputed using the KNN algorithm.
            """
        # Ensure the input is a DataFrame
        if not isinstance(dna_m, pd.DataFrame):
            raise ValueError("Input must be a pandas DataFrame")

        # Perform KNN imputation
        imputer = KNN(n_neighbors=self.n_neighbors)
        return pd.DataFrame(imputer.fit_transform(dna_m), columns=dna_m.columns)
