import unittest
from unittest.mock import patch

import pandas as pd

from epygenetics.clocks.biological_age_and_mortality_predictors.non_prc_pheno_age import \
    NonPRCPhenoAgeClock
from epygenetics.clocks.type import ClockType


class NonPRCPhenoAgeClockTestCase(unittest.TestCase):

    @patch('pandas.read_csv')
    def test_initialization(self, mock_read_csv):
        """Test the initialization of NonPRCPhenoAgeClock."""
        # Mock the CpG DataFrame
        mock_cpgs = pd.DataFrame({
            'CpG': ['cg00000029', 'cg00000108', 'cg00000109'],
            'Weight': [0.1, 0.2, 0.3]
        })
        mock_read_csv.return_value = mock_cpgs

        # Initialize the clock
        clock = NonPRCPhenoAgeClock()

        # Assert that the CSV file was read correctly
        mock_read_csv.assert_called_once_with('data/CpGs/non_prcPhenoAge.csv')

        # Assert that the attributes are set correctly
        self.assertEqual(clock.name, ClockType.NON_PRC_PHENO_AGE)
        self.assertEqual(clock.marker_name, 'CpG')
        self.assertEqual(clock.coef_name, 'Weight')
        self.assertEqual(clock.reg_coef, 0)
        pd.testing.assert_frame_equal(clock.cpgs, mock_cpgs)

    @patch('pandas.read_csv')
    def test_initialization_csv_missing(self, mock_read_csv):
        """Test initialization when the CSV file is missing."""
        # Simulate a FileNotFoundError
        mock_read_csv.side_effect = FileNotFoundError

        with self.assertRaises(FileNotFoundError):
            NonPRCPhenoAgeClock()


if __name__ == '__main__':
    unittest.main()
