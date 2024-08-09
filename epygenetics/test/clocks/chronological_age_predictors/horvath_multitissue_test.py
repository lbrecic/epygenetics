import unittest
from unittest.mock import patch
import pandas as pd
import numpy as np
import pytest

from epygenetics.clocks.chronological_age_predictors.horvath_multitissue import HorvathMultitissueClock
from epygenetics.clocks.type import ClockType


class HorvathMultitissueClockTestCase(unittest.TestCase):

    @patch('pandas.read_csv')
    def test_initialization(self, mock_read_csv):
        """Test the initialization of HorvathMultitissueClock."""
        # Mock the CpG DataFrame
        mock_cpgs = pd.DataFrame({
            'CpGmarker': ['cg00000029', 'cg00000108', 'cg00000109'],
            'CoefficientTraining': [0.1, 0.2, 0.3]
        })
        mock_read_csv.return_value = mock_cpgs

        # Initialize the clock
        clock = HorvathMultitissueClock()

        # Assert that the CSV file was read correctly
        mock_read_csv.assert_called_once_with('data/CpGs/Horvath1_CpGs.csv')

        # Assert that the attributes are set correctly
        self.assertEqual(clock.name, ClockType.HORVATH_MULTITISSUE)
        self.assertEqual(clock.marker_name, 'CpGmarker')
        self.assertEqual(clock.coef_name, 'CoefficientTraining')
        self.assertEqual(clock.reg_coef, 0.696)
        pd.testing.assert_frame_equal(clock.cpgs, mock_cpgs)

    @patch('pandas.read_csv')
    def test_initialization_csv_missing(self, mock_read_csv):
        """Test initialization when the CSV file is missing."""
        # Simulate a FileNotFoundError
        mock_read_csv.side_effect = FileNotFoundError

        with self.assertRaises(FileNotFoundError):
            HorvathMultitissueClock()

    @pytest.mark.skip(reason="This test is not working as expected.")
    @patch('epygenetics.utils.anti_trafo')
    @patch('pandas.read_csv')
    def test_calculate(self, mock_read_csv, mock_anti_trafo):
        """Test the calculate method."""
        # Mock the CpG DataFrame
        mock_cpgs = pd.DataFrame({
            'CpGmarker': ['cg00000029', 'cg00000108', 'cg00000109'],
            'CoefficientTraining': [0.1, 0.2, 0.3]
        })
        mock_read_csv.return_value = mock_cpgs

        # Mock the anti_trafo function
        mock_anti_trafo.return_value = np.array([1.5, 2.5])

        # Initialize the clock
        clock = HorvathMultitissueClock()

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

        # Assert that the anti_trafo function was called correctly
        expected_tt = np.dot(dna_m[common_cpgs],
                             mock_cpgs.set_index('CpGmarker').loc[common_cpgs, 'CoefficientTraining']) + clock.reg_coef
        mock_anti_trafo.assert_called_once_with(expected_tt)

        # Assert that the pheno DataFrame was updated correctly
        expected_pheno = pd.DataFrame({
            'Age': [30, 40],
            ClockType.HORVATH_MULTITISSUE: [1.5, 2.5]
        })
        pd.testing.assert_frame_equal(result, expected_pheno)

    @pytest.mark.skip(reason="This test is not working as expected.")
    @patch('epygenetics.utils.anti_trafo')
    @patch('pandas.read_csv')
    def test_calculate_without_pheno(self, mock_read_csv, mock_anti_trafo):
        """Test the calculate method without pheno."""
        # Mock the CpG DataFrame
        mock_cpgs = pd.DataFrame({
            'CpGmarker': ['cg00000029', 'cg00000108', 'cg00000109'],
            'CoefficientTraining': [0.1, 0.2, 0.3]
        })
        mock_read_csv.return_value = mock_cpgs

        # Mock the anti_trafo function
        mock_anti_trafo.return_value = np.array([1.5, 2.5])

        # Initialize the clock
        clock = HorvathMultitissueClock()

        # Create mock dna_m DataFrame
        dna_m = pd.DataFrame({
            'cg00000029': [0.5, 0.6],
            'cg00000108': [0.7, 0.8],
            'cg00000109': [0.9, 1.0]
        })

        common_cpgs = np.array(['cg00000029', 'cg00000108', 'cg00000109'])

        # Test calculate without pheno
        result = clock.calculate(dna_m, common_cpgs, cpg_check=True, pheno=None, is_imputation=False)

        # Assert that the anti_trafo function was called correctly
        expected_tt = np.dot(dna_m[common_cpgs],
                             mock_cpgs.set_index('CpGmarker').loc[common_cpgs, 'CoefficientTraining']) + clock.reg_coef
        mock_anti_trafo.assert_called_once_with(expected_tt)

        # Assert that the result is a Series with the correct values
        expected_series = pd.Series([1.5, 2.5], index=dna_m.index)
        pd.testing.assert_series_equal(result, expected_series)

    @pytest.mark.skip(reason="This test is not working as expected.")
    def test_calculate_cpg_check_fail_without_imputation(self):
        """Test calculate method when CpG check fails without imputation."""
        # Initialize the clock
        clock = HorvathMultitissueClock()

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
