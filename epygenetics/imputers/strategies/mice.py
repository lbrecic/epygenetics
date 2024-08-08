import pandas as pd
import numpy as np
from sklearn.experimental import enable_iterative_imputer  # noqa
from sklearn.ensemble import HistGradientBoostingRegressor

from epygenetics.imputers.base_imputer import BaseImputer


class MICEImputer(BaseImputer):
    def __init__(self, max_iter=10, random_state=None):
        self.max_iter = max_iter
        self.random_state = random_state

    def impute(self, dna_m: pd.DataFrame) -> pd.DataFrame:
        """
        This function imputes missing values in a pandas DataFrame using a custom row-wise MICE algorithm.

        Parameters:
        dna_m (pd.DataFrame): The input DataFrame with missing values.
        max_iter (int): Maximum number of imputation iterations (default is 10).
        random_state (int): Random state for reproducibility (default is None).

        Returns:
        pd.DataFrame: A DataFrame with missing values imputed using the custom MICE algorithm.
        """
        for iteration in range(self.max_iter):
            for col in dna_m.columns:
                if dna_m[col].isna().any():
                    # Iterate over each row with NaN values in the current column
                    for row_idx in dna_m.index[dna_m[col].isna()]:
                        row = dna_m.loc[row_idx]
                        non_nan_cols = row.index[~row.isna()]

                        if len(non_nan_cols) == 0:
                            continue  # Skip if all values in the row are NaN

                        X_train = dna_m.loc[dna_m.index != row_idx, non_nan_cols].values
                        y_train = dna_m.loc[dna_m.index != row_idx, col].values

                        # Remove rows with NaN in the target column for training
                        mask = ~np.isnan(y_train)
                        X_train = X_train[mask]
                        y_train = y_train[mask]

                        if len(y_train) == 0:
                            continue  # Skip if there are no valid training samples

                        X_test = row[non_nan_cols].values.reshape(1, -1)

                        # Fit the model
                        model = HistGradientBoostingRegressor(random_state=self.random_state)
                        model.fit(X_train, y_train)

                        # Predict the missing value
                        imputed_value = model.predict(X_test)[0]
                        dna_m.at[row_idx, col] = imputed_value

        return dna_m
