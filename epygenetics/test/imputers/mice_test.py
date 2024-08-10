import unittest

import numpy as np
import pandas as pd

from epygenetics.imputers.strategies.mice import MICEImputer


class MICEImputerTestCase(unittest.TestCase):

    def setUp(self):
        """Set up for the tests with an example DataFrame containing missing values."""
        self.dna_m = pd.DataFrame({
            'A': [1.0, np.nan, 3.0, 4.0],
            'B': [2.0, 3.0, np.nan, 1.0],
            'C': [np.nan, 5.0, np.nan, 2.0],
            'D': [4.0, 1.0, 2.0, np.nan]
        })

    def test_impute_mice(self):
        """Test the imputation using MICE algorithm."""
        imputer = MICEImputer(max_iter=5, random_state=42)
        imputed_dna_m = imputer.impute(self.dna_m.copy())

        # Check that no NaN values remain after imputation
        self.assertFalse(imputed_dna_m.isnull().values.any(), "There should be no NaN values after imputation.")

    def test_impute_all_nan_row(self):
        """Test imputation when a row is completely NaN."""
        dna_m_all_nan = pd.DataFrame({
            'A': [np.nan, 2.0, 3.0, 4.0],
            'B': [np.nan, 3.0, np.nan, 1.0],
            'C': [np.nan, 5.0, np.nan, 2.0],
            'D': [np.nan, 1.0, 2.0, np.nan]
        })
        imputer = MICEImputer(max_iter=5, random_state=42)
        imputed_dna_m = imputer.impute(dna_m_all_nan.copy())

        # Verify that the row with all NaN remains unchanged
        self.assertTrue(imputed_dna_m.iloc[0].isnull().all(), "The row with all NaN should remain unchanged.")

    def test_impute_no_nan(self):
        """Test imputation when there are no NaN values."""
        dna_m_no_nan = pd.DataFrame({
            'A': [1.0, 2.0, 3.0, 4.0],
            'B': [2.0, 3.0, 4.0, 1.0],
            'C': [3.0, 5.0, 6.0, 2.0],
            'D': [4.0, 1.0, 2.0, 3.0]
        })
        imputer = MICEImputer(max_iter=5, random_state=42)
        imputed_dna_m = imputer.impute(dna_m_no_nan.copy())

        # Verify that the DataFrame is unchanged
        pd.testing.assert_frame_equal(imputed_dna_m, dna_m_no_nan, check_dtype=False)

    def test_impute_single_nan_column(self):
        """Test imputation when only one column contains NaN values."""
        dna_m_single_nan_col = pd.DataFrame({
            'A': [1.0, 2.0, np.nan, 4.0],
            'B': [2.0, 3.0, 4.0, 1.0],
            'C': [3.0, 5.0, 6.0, 2.0],
            'D': [4.0, 1.0, 2.0, 3.0]
        })
        imputer = MICEImputer(max_iter=5, random_state=42)
        imputed_dna_m = imputer.impute(dna_m_single_nan_col.copy())

        # Ensure no NaN values remain after imputation
        self.assertFalse(imputed_dna_m.isnull().values.any(),
                         "There should be no NaN values after imputation in a single column.")

    def test_impute_single_row(self):
        """Test imputation when there's only a single row with missing data."""
        dna_m_single_row = pd.DataFrame({
            'A': [np.nan],
            'B': [3.0],
            'C': [5.0],
            'D': [np.nan]
        })
        imputer = MICEImputer(max_iter=5, random_state=42)
        imputed_dna_m = imputer.impute(dna_m_single_row.copy())

        # Since only one row exists, imputation should not change anything (no other data to impute from)
        pd.testing.assert_frame_equal(imputed_dna_m, dna_m_single_row, check_dtype=False)


if __name__ == '__main__':
    unittest.main()
