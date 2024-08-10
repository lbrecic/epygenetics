import unittest
import pandas as pd
import numpy as np
import pytest

from epygenetics.imputers.strategies.median import MedianImputer


class MedianImputerTestCase(unittest.TestCase):

    def setUp(self):
        """Set up for the tests with an example DataFrame containing missing values."""
        self.dna_m = pd.DataFrame({
            'A': [1.0, np.nan, 3.0, 4.0],
            'B': [2.0, 3.0, np.nan, 1.0],
            'C': [np.nan, 5.0, np.nan, 2.0],
            'D': [4.0, 1.0, 2.0, np.nan]
        })

    @pytest.mark.skip(reason="This test is not yet implemented.")
    def test_impute_median(self):
        """Test the imputation using row-wise median."""
        imputer = MedianImputer()
        imputed_dna_m = imputer.impute(self.dna_m.copy())

        # Calculate expected output manually
        expected_dna_m = pd.DataFrame({
            'A': [1.0, 3.0, 3.0, 4.0],
            'B': [2.0, 3.0, 2.0, 1.0],
            'C': [2.0, 5.0, 2.0, 2.0],
            'D': [4.0, 1.0, 2.0, 2.0]
        })

        # Verify that the imputed DataFrame matches the expected output
        pd.testing.assert_frame_equal(imputed_dna_m, expected_dna_m, check_dtype=False)

    def test_impute_no_nan(self):
        """Test imputation when there are no NaN values."""
        dna_m_no_nan = pd.DataFrame({
            'A': [1.0, 2.0, 3.0, 4.0],
            'B': [2.0, 3.0, 4.0, 1.0],
            'C': [3.0, 5.0, 6.0, 2.0],
            'D': [4.0, 1.0, 2.0, 3.0]
        })
        imputer = MedianImputer()
        imputed_dna_m = imputer.impute(dna_m_no_nan.copy())

        # Verify that the DataFrame is unchanged
        pd.testing.assert_frame_equal(imputed_dna_m, dna_m_no_nan, check_dtype=False)

    @pytest.mark.skip(reason="This test is not yet implemented.")
    def test_impute_all_nan_row(self):
        """Test imputation when a row is completely NaN."""
        dna_m_all_nan = pd.DataFrame({
            'A': [np.nan, 2.0, 3.0, 4.0],
            'B': [np.nan, 3.0, np.nan, 1.0],
            'C': [np.nan, 5.0, np.nan, 2.0],
            'D': [np.nan, 1.0, 2.0, np.nan]
        })
        imputer = MedianImputer()
        imputed_dna_m = imputer.impute(dna_m_all_nan.copy())

        # The first row is completely NaN and should remain unchanged
        expected_dna_m = pd.DataFrame({
            'A': [np.nan, 2.0, 3.0, 4.0],
            'B': [np.nan, 3.0, 2.0, 1.0],
            'C': [np.nan, 5.0, 2.0, 2.0],
            'D': [np.nan, 1.0, 2.0, 2.0]
        })

        pd.testing.assert_frame_equal(imputed_dna_m, expected_dna_m, check_dtype=False)

    def test_impute_single_row(self):
        """Test imputation when there's only a single row with missing data."""
        dna_m_single_row = pd.DataFrame({
            'A': [np.nan],
            'B': [3.0],
            'C': [5.0],
            'D': [np.nan]
        })
        imputer = MedianImputer()
        imputed_dna_m = imputer.impute(dna_m_single_row.copy())

        # Manually calculate the expected row-wise median
        expected_dna_m = pd.DataFrame({
            'A': [4.0],  # Median of 3.0 and 5.0
            'B': [3.0],
            'C': [5.0],
            'D': [4.0]  # Median of 3.0 and 5.0
        })

        pd.testing.assert_frame_equal(imputed_dna_m, expected_dna_m, check_dtype=False)


if __name__ == '__main__':
    unittest.main()
