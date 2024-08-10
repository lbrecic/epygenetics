import unittest
from unittest.mock import MagicMock, patch

import numpy as np
import pandas as pd
import pytest

from epygenetics.clocks.base_clocks.linear_clock import LinearClock
from epygenetics.imputers.base_imputer import BaseImputer
from epygenetics.imputers.type import ImputerType


class LinearClockTestCase(unittest.TestCase):

    def setUp(self):
        """Set up the LinearClock instance for testing."""
        self.cpgs_data = pd.DataFrame({
            'marker_name': ['cpg1', 'cpg2', 'cpg3']
        })
        self.clock = LinearClock(name="TestLinearClock", marker_name="marker_name", cpgs=self.cpgs_data)

    def test_initialization(self):
        """Test the initialization of LinearClock."""
        self.assertEqual(self.clock.name, "TestLinearClock")
        self.assertEqual(self.clock.marker_name, "marker_name")
        pd.testing.assert_frame_equal(self.clock.cpgs, self.cpgs_data)

    def test_check_cpgs_no_imputation(self):
        """Test check_cpgs when all CpGs are present and no imputation is required."""
        dna_m = pd.DataFrame({
            'cpg1': [0.1, 0.2],
            'cpg2': [0.3, 0.4],
            'cpg3': [0.5, 0.6]
        })
        present_cpgs, cpg_check = self.clock.check_cpgs(dna_m)
        self.assertTrue(cpg_check)
        np.testing.assert_array_equal(present_cpgs, np.array(['cpg1', 'cpg2', 'cpg3']))

    @patch('epygenetics.imputers.factory.ImputerFactory.create_imputer')
    def test_check_cpgs_with_imputation(self, mock_create_imputer):
        """Test check_cpgs when CpGs are missing and imputation is required."""
        dna_m = pd.DataFrame({
            'cpg1': [0.1, 0.2],
            'cpg2': [0.3, 0.4]
        })
        cpg_imputation = pd.DataFrame({
            'marker_name': ['cpg3'],
            'mean_value': [0.5]
        })

        # Mock the imputer
        mock_imputer = MagicMock(spec=BaseImputer)
        mock_create_imputer.return_value = mock_imputer

        present_cpgs, cpg_check = self.clock.check_cpgs(dna_m, is_imputation=True, imputer_type=ImputerType.REGULAR,
                                                        cpg_imputation=cpg_imputation)

        # Assert that imputation was triggered and applied correctly
        self.assertFalse(cpg_check)
        self.assertIn('cpg3', dna_m.columns)
        np.testing.assert_array_equal(present_cpgs, np.array(['cpg1', 'cpg2', 'cpg3']))
        mock_imputer.impute.assert_called_once_with(dna_m)

    def test_check_cpgs_missing_imputation_data(self):
        """Test check_cpgs when necessary imputation data is missing."""
        dna_m = pd.DataFrame({
            'cpg1': [0.1, 0.2],
            'cpg2': [0.3, 0.4]
        })

        with self.assertRaises(ValueError) as context:
            self.clock.check_cpgs(dna_m, is_imputation=True, imputer_type=ImputerType.REGULAR, cpg_imputation=None)

        self.assertIn("Necessary CpG is missing and no imputation data provided!", str(context.exception))

    def test_calculate_with_cpg_check(self):
        """Test calculate method when CpGs are present."""
        dna_m = pd.DataFrame({
            'cpg1': [0.1, 0.2],
            'cpg2': [0.3, 0.4],
            'cpg3': [0.5, 0.6]
        })
        present_cpgs = np.array(['cpg1', 'cpg2', 'cpg3'])
        result = self.clock.calculate(dna_m, present_cpgs, cpg_check=True, pheno=None, is_imputation=False)

        expected_data = dna_m[present_cpgs]
        pd.testing.assert_frame_equal(result, expected_data)

    @pytest.mark.skip("Not implemented yet")
    def test_calculate_with_pheno(self):
        """Test calculate method when CpGs are present and pheno is provided."""
        dna_m = pd.DataFrame({
            'cpg1': [0.1, 0.2],
            'cpg2': [0.3, 0.4],
            'cpg3': [0.5, 0.6]
        })
        pheno = pd.DataFrame({'Age': [30, 40]})
        present_cpgs = np.array(['cpg1', 'cpg2', 'cpg3'])
        result = self.clock.calculate(dna_m, present_cpgs, cpg_check=True, pheno=pheno, is_imputation=False)

        # Create the expected DataFrame with the CpG values as individual columns
        expected_pheno = pheno.copy()
        expected_pheno['TestLinearClock'] = [list(row) for row in dna_m[present_cpgs].values]

        pd.testing.assert_frame_equal(result, expected_pheno)

    @pytest.mark.skip("Not implemented yet")
    def test_calculate_cpg_check_fail_without_imputation(self):
        """Test calculate method when CpGs do not match and imputation is not enabled."""
        dna_m = pd.DataFrame({
            'cpg1': [0.1, 0.2],
            'cpg2': [0.3, 0.4]
        })
        present_cpgs = np.array(['cpg1', 'cpg2', 'cpg3'])

        with self.assertRaises(Exception) as context:
            self.clock.calculate(dna_m, present_cpgs, cpg_check=False, pheno=None, is_imputation=False)

        self.assertIn("CpG Check failed and imputation is not enabled or feasible.", str(context.exception))


if __name__ == '__main__':
    unittest.main()
