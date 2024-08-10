import unittest
from unittest.mock import MagicMock, patch

import numpy as np
import pandas as pd

from epygenetics.clocks.base_clocks.regression_clock import RegressionClock
from epygenetics.imputers.base_imputer import BaseImputer


class RegressionClockTestCase(unittest.TestCase):

    def setUp(self):
        """Set up the RegressionClock instance for testing."""
        cpgs_data = pd.DataFrame({
            'marker_name': ['cpg1', 'cpg2', 'cpg3'],
            'coef_name': [0.1, 0.2, 0.3]
        })
        self.clock = RegressionClock(name="TestClock", marker_name="marker_name", coef_name="coef_name", reg_coef=5.0, cpgs=cpgs_data)

    def test_initialization(self):
        """Test the initialization of RegressionClock."""
        self.assertEqual(self.clock.name, "TestClock")
        self.assertEqual(self.clock.marker_name, "marker_name")
        self.assertEqual(self.clock.coef_name, "coef_name")
        self.assertEqual(self.clock.reg_coef, 5.0)
        pd.testing.assert_frame_equal(self.clock.cpgs, pd.DataFrame({
            'marker_name': ['cpg1', 'cpg2', 'cpg3'],
            'coef_name': [0.1, 0.2, 0.3]
        }))

    def test_check_cpgs_no_imputation(self):
        """Test check_cpgs when all CpGs match and no imputation is required."""
        dna_m = pd.DataFrame({
            'cpg1': [0.1, 0.2],
            'cpg2': [0.3, 0.4],
            'cpg3': [0.5, 0.6]
        })
        common_cpgs, cpg_check = self.clock.check_cpgs(dna_m)
        self.assertTrue(cpg_check)
        np.testing.assert_array_equal(common_cpgs, np.array(['cpg1', 'cpg2', 'cpg3']))

    @patch('epygenetics.imputers.factory.ImputerFactory.create_imputer')
    def test_check_cpgs_with_imputation(self, mock_create_imputer):
        """Test check_cpgs when CpGs do not match and imputation is required."""
        dna_m = pd.DataFrame({
            'cpg1': [0.1, 0.2],
            'cpg2': [0.3, 0.4]
        })

        mock_imputer = MagicMock(spec=BaseImputer)
        mock_create_imputer.return_value = mock_imputer

        common_cpgs, cpg_check = self.clock.check_cpgs(dna_m, is_imputation=True)
        self.assertFalse(cpg_check)
        self.assertTrue('cpg3' in dna_m.columns)
        mock_imputer.impute.assert_called_once_with(dna_m)
        np.testing.assert_array_equal(common_cpgs, np.array(['cpg1', 'cpg2', 'cpg3']))

    def test_calculate_with_cpg_check(self):
        """Test calculate method when CpGs match (cpg_check=True)."""
        dna_m = pd.DataFrame({
            'cpg1': [0.1, 0.2],
            'cpg2': [0.3, 0.4],
            'cpg3': [0.5, 0.6]
        })

        common_cpgs = np.array(['cpg1', 'cpg2', 'cpg3'])
        result = self.clock.calculate(dna_m, common_cpgs, cpg_check=True, pheno=None, is_imputation=False)

        expected_values = np.dot(dna_m[common_cpgs], np.array([0.1, 0.2, 0.3])) + 5.0
        pd.testing.assert_series_equal(result, pd.Series(expected_values, index=dna_m.index))

    def test_calculate_with_pheno(self):
        """Test calculate method when CpGs match and pheno DataFrame is provided."""
        dna_m = pd.DataFrame({
            'cpg1': [0.1, 0.2],
            'cpg2': [0.3, 0.4],
            'cpg3': [0.5, 0.6]
        })

        pheno = pd.DataFrame({'Age': [30, 40]})

        common_cpgs = np.array(['cpg1', 'cpg2', 'cpg3'])
        result = self.clock.calculate(dna_m, common_cpgs, cpg_check=True, pheno=pheno, is_imputation=False)

        expected_values = np.dot(dna_m[common_cpgs], np.array([0.1, 0.2, 0.3])) + 5.0
        pheno['TestClock'] = expected_values
        pd.testing.assert_frame_equal(result, pheno)

    def test_calculate_cpg_check_fail_without_imputation(self):
        """Test calculate method when CpGs do not match and imputation is not enabled."""
        dna_m = pd.DataFrame({
            'cpg1': [0.1, 0.2],
            'cpg2': [0.3, 0.4]
        })

        common_cpgs = np.array(['cpg1', 'cpg2', 'cpg3'])

        with self.assertRaises(Exception) as context:
            self.clock.calculate(dna_m, common_cpgs, cpg_check=False, pheno=None, is_imputation=False)

        self.assertTrue("CpG Check failed and imputation is not enabled or feasible." in str(context.exception))


if __name__ == '__main__':
    unittest.main()
