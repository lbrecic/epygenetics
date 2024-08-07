import numpy as np
import pandas as pd
from sklearn.metrics import nan_euclidean_distances

from epygenetics.imputers.base_imputer import BaseImputer


class KNNImputer(BaseImputer):
    def __init__(self, n_neighbors: int = 5) -> None:
        self.n_neighbors: int = n_neighbors

    def impute(self, dna_m: pd.DataFrame) -> pd.DataFrame:
        """
        This function imputes missing values in a pandas DataFrame using a column-wise K-Nearest Neighbors algorithm.

        Parameters:
        df (pd.DataFrame): The input DataFrame with missing values.
        n_neighbors (int): Number of neighboring columns to use for imputation (default is 5).

        Returns:
        pd.DataFrame: A DataFrame with missing values imputed using the KNN algorithm.
        """
        dna_m_imputed = dna_m.copy()

        for col in dna_m.columns:
            if dna_m[col].isna().any():
                # Compute the distance between columns
                distances = nan_euclidean_distances(dna_m.T)
                col_index = dna_m.columns.get_loc(col)
                distances[col_index, col_index] = np.inf  # Ignore self-distance

                # Find the indices of the n-nearest neighboring columns
                neighbors_idx = np.argsort(distances[col_index])[:self.n_neighbors]

                # Calculate the mean of the neighboring columns for each row
                for row in dna_m.index[dna_m[col].isna()]:
                    neighbor_values = dna_m.iloc[row, neighbors_idx].dropna()
                    if not neighbor_values.empty:
                        dna_m_imputed.at[row, col] = neighbor_values.mean()

        return dna_m_imputed
