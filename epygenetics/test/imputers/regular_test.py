import unittest

import numpy as np
import pandas as pd
import pytest

from epygenetics.imputers.strategies.regular import RegularImputer


class RegularImputerTestCase(unittest.TestCase):

    def setUp(self):
        """Set up for the tests with example DataFrames containing missing values and imputation values."""
        self.dna_m = pd.DataFrame({
            'CpG1': [np.nan, np.nan, np.nan],
            'CpG2': [2.0, 3.0, 4.0],
            'CpG3': [np.nan, 5.0, 6.0],
        })

        self.cpg_imputation = pd.DataFrame({
            'CpG': ['CpG1', 'CpG3'],
            'ImputationValue': [1.5, 5.5]
        })

    @pytest.mark.skip(reason="This test is not yet implemented.")
    def test_impute_regular(self):
        """Test the imputation using Regular Imputer."""
        imputer = RegularImputer(cpg_imputation=self.cpg_imputation)
        imputed_dna_m = imputer.impute(self.dna_m.copy())

        # Expected DataFrame after imputation
        expected_dna_m = pd.DataFrame({
            'CpG1': [1.5, 1.5, 1.5],
            'CpG2': [2.0, 3.0, 4.0],
            'CpG3': [5.5, 5.0, 6.0],
        })

        # Verify that the imputed DataFrame matches the expected output
        pd.testing.assert_frame_equal(imputed_dna_m, expected_dna_m, check_dtype=False)

    def test_no_imputation_needed(self):
        """Test the case where no columns need imputation."""
        dna_m_no_nan = pd.DataFrame({
            'CpG1': [1.0, 2.0, 3.0],
            'CpG2': [2.0, 3.0, 4.0],
            'CpG3': [3.0, 5.0, 6.0],
        })
        imputer = RegularImputer(cpg_imputation=self.cpg_imputation)
        imputed_dna_m = imputer.impute(dna_m_no_nan.copy())

        # Verify that the DataFrame is unchanged
        pd.testing.assert_frame_equal(imputed_dna_m, dna_m_no_nan, check_dtype=False)

    def test_all_nan_columns_imputation(self):
        """Test the case where a column with all NaN values is imputed."""
        dna_m_all_nan = pd.DataFrame({
            'CpG1': [np.nan, np.nan, np.nan],
            'CpG2': [np.nan, np.nan, np.nan],
            'CpG3': [np.nan, np.nan, np.nan],
        })

        cpg_imputation_all_nan = pd.DataFrame({
            'CpG': ['CpG1', 'CpG2', 'CpG3'],
            'ImputationValue': [1.5, 2.5, 3.5]
        })

        imputer = RegularImputer(cpg_imputation=cpg_imputation_all_nan)
        imputed_dna_m = imputer.impute(dna_m_all_nan.copy())

        # Expected DataFrame after imputation
        expected_dna_m = pd.DataFrame({
            'CpG1': [1.5, 1.5, 1.5],
            'CpG2': [2.5, 2.5, 2.5],
            'CpG3': [3.5, 3.5, 3.5],
        })

        # Verify that the imputed DataFrame matches the expected output
        pd.testing.assert_frame_equal(imputed_dna_m, expected_dna_m, check_dtype=False)

    def test_invalid_inputs(self):
        """Test the case where the inputs are not DataFrames."""
        with self.assertRaises(ValueError):
            imputer = RegularImputer(cpg_imputation=None)
            imputer.impute(self.dna_m.copy())

        with self.assertRaises(ValueError):
            imputer = RegularImputer(cpg_imputation=self.cpg_imputation)
            imputer.impute(None)


if __name__ == '__main__':
    unittest.main()
