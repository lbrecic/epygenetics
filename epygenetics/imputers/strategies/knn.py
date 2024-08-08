import numpy as np
import pandas as pd
from sklearn.neighbors import NearestNeighbors

from epygenetics.imputers.base_imputer import BaseImputer


class KNNImputer(BaseImputer):
    def __init__(self, n_neighbors: int = 5) -> None:
        self.n_neighbors: int = n_neighbors

    def impute(self, dna_m: pd.DataFrame) -> pd.DataFrame:
        """
        This function imputes missing values in a pandas DataFrame using a row-wise K-Nearest Neighbors algorithm.

        Parameters:
        dna_m (pd.DataFrame): The input DataFrame with missing values.
        n_neighbors (int): Number of neighboring columns to use for imputation (default is 5).

        Returns:
        pd.DataFrame: A DataFrame with missing values imputed using the KNN algorithm.
        """
        # Iterate over each row in the DataFrame
        for row_idx in dna_m.index:
            row = dna_m.loc[row_idx]

            # Identify columns with and without NaN values
            nan_cols = row.index[row.isna()]
            non_nan_cols = row.index[~row.isna()]

            if len(non_nan_cols) == 0:
                continue  # If all values in the row are NaN, skip imputation

            # Extract non-NaN values
            non_nan_values = row[non_nan_cols].values.reshape(1, -1)

            # Fit NearestNeighbors model on non-NaN values
            knn = NearestNeighbors(n_neighbors=min(self.n_neighbors, len(non_nan_values[0])))
            knn.fit(np.arange(len(non_nan_values[0])).reshape(-1, 1), non_nan_values[0].reshape(-1, 1))

            # Predict NaN values based on k nearest neighbors
            for col in nan_cols:
                col_idx = dna_m.columns.get_loc(col)
                distances, indices = knn.kneighbors([[col_idx]], return_distance=True)
                nearest_indices = indices.flatten()

                # Compute the mean of the nearest neighbors
                neighbor_values = non_nan_values[0][nearest_indices]
                imputed_value = np.mean(neighbor_values)

                # Update the imputed DataFrame
                dna_m.at[row_idx, col] = imputed_value

        return dna_m
