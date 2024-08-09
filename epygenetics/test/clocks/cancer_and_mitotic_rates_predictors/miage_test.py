import unittest
from unittest.mock import patch
import pandas as pd
import numpy as np
import pytest

from epygenetics.clocks.cancer_and_mitotic_rates_predictors.miage import MiAgeClock
from epygenetics.clocks.type import ClockType

@pytest.mark.skip(reason="Test is not implemented yet")
class MiAgeClockTestCase(unittest.TestCase):

    @patch('pandas.read_csv')
    def test_initialization(self, mock_read_csv):
        """Test the initialization of MiAgeClock."""
        # Mock the CpG DataFrame
        mock_cpgs = pd.DataFrame({
            'CpGs': ['cg00000029', 'cg00000108', 'cg00000109'],
            'Age-hyper/Age-hypo': [0.1, 0.2, 0.3]
        })
        mock_read_csv.return_value = mock_cpgs

        # Initialize the clock
        clock = MiAgeClock('param1', 'param2')

        # Assert that the CSV file was read correctly
        mock_read_csv.assert_called_once_with('data/CpGs/MiAge_CpGs.csv')

        # Assert that the attributes are set correctly
        self.assertEqual(clock.name, ClockType.MIAGE)
        self.assertEqual(clock.marker_name, 'CpGs')
        self.assertEqual(clock.coef_name, 'Age-hyper/Age-hypo')
        self.assertEqual(clock.reg_coef, 0)
        self.assertEqual(clock.miage_params, ('param1', 'param2'))
        pd.testing.assert_frame_equal(clock.cpgs, mock_cpgs)

    @patch('pandas.read_csv')
    def test_initialization_csv_missing(self, mock_read_csv):
        """Test initialization when the CSV file is missing."""
        # Simulate a FileNotFoundError
        mock_read_csv.side_effect = FileNotFoundError

        with self.assertRaises(FileNotFoundError):
            MiAgeClock()

    @patch('epygenetics.utils.mi_age_mitotic_age')
    @patch('pandas.read_csv')
    def test_calculate(self, mock_read_csv, mock_miage_mitotic_age):
        """Test the calculate method."""
        # Mock the CpG DataFrame
        mock_cpgs = pd.DataFrame({
            'CpGs': ['cg00000029', 'cg00000108', 'cg00000109'],
            'Age-hyper/Age-hypo': [0.1, 0.2, 0.3]
        })
        mock_read_csv.return_value = mock_cpgs

        # Mock the miage_mitotic_age function
        mock_miage_mitotic_age.return_value = np.array([1.5, 2.5])

        # Initialize the clock
        clock = MiAgeClock('param1', 'param2')

        # Create mock dna_m DataFrame
        dna_m = pd.DataFrame({
            'cg00000029': [0.5, 0.6],
            'cg00000108': [0.7, 0.8],
            'cg00000109': [0.9, 1.0]
        })

        common_cpgs = np.array(['cg00000029', 'cg00000108', 'cg00000109'])

        # Test calculate with pheno provided
        pheno = pd.DataFrame({'Age': [30, 40]})
        result = clock.calculate(dna_m, common_cpgs, cpg_check=True, pheno=pheno, is_imputation=False)

        # Assert that the miage_mitotic_age function was called correctly
        transposed_data = dna_m[common_cpgs].T
        mock_miage_mitotic_age.assert_called_once_with(transposed_data, 'param1', 'param2')

        # Assert that the pheno DataFrame was updated correctly
        expected_pheno = pd.DataFrame({
            'Age': [30, 40],
            ClockType.MIAGE: [1.5, 2.5]
        })
        pd.testing.assert_frame_equal(result, expected_pheno)

    @patch('epygenetics.utils.mi_age_mitotic_age')
    @patch('pandas.read_csv')
    def test_calculate_without_pheno(self, mock_read_csv, mock_miage_mitotic_age):
        """Test the calculate method without pheno."""
        # Mock the CpG DataFrame
        mock_cpgs = pd.DataFrame({
            'CpGs': ['cg00000029', 'cg00000108', 'cg00000109'],
            'Age-hyper/Age-hypo': [0.1, 0.2, 0.3]
        })
        mock_read_csv.return_value = mock_cpgs

        # Mock the miage_mitotic_age function
        mock_miage_mitotic_age.return_value = np.array([1.5, 2.5])

        # Initialize the clock
        clock = MiAgeClock('param1', 'param2')

        # Create mock dna_m DataFrame
        dna_m = pd.DataFrame({
            'cg00000029': [0.5, 0.6],
            'cg00000108': [0.7, 0.8],
            'cg00000109': [0.9, 1.0]
        })

        common_cpgs = np.array(['cg00000029', 'cg00000108', 'cg00000109'])

        # Test calculate without pheno
        result = clock.calculate(dna_m, common_cpgs, cpg_check=True, pheno=None, is_imputation=False)

        # Assert that the miage_mitotic_age function was called correctly
        transposed_data = dna_m[common_cpgs].T
        mock_miage_mitotic_age.assert_called_once_with(transposed_data, 'param1', 'param2')

        # Assert that the result is a Series with the correct values
        expected_series = pd.Series([1.5, 2.5], index=dna_m.index)
        pd.testing.assert_series_equal(result, expected_series)

    def test_calculate_cpg_check_fail_without_imputation(self):
        """Test calculate method when CpG check fails without imputation."""
        # Initialize the clock
        clock = MiAgeClock('param1', 'param2')

        # Create mock dna_m DataFrame
        dna_m = pd.DataFrame({
            'cg00000029': [0.5, 0.6],
            'cg00000108': [0.7, 0.8]
        })

        common_cpgs = np.array(['cg00000029', 'cg00000108', 'cg00000109'])

        with self.assertRaises(Exception) as context:
            clock.calculate(dna_m, common_cpgs, cpg_check=False, pheno=None, is_imputation=False)

        self.assertIn("CpG Check failed and imputation is not enabled or feasible.", str(context.exception))


if __name__ == '__main__':
    unittest.main()
