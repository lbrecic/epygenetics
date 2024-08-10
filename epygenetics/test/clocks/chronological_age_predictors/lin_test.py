import unittest
from unittest.mock import patch

import pandas as pd

from epygenetics.clocks.chronological_age_predictors.lin import LinClock
from epygenetics.clocks.type import ClockType


class LinClockTestCase(unittest.TestCase):

    @patch('pandas.read_csv')
    def test_initialization(self, mock_read_csv):
        """Test the initialization of LinClock."""
        # Mock the CpG DataFrame
        mock_cpgs = pd.DataFrame({
            'id': ['cg00000029', 'cg00000108', 'cg00000109'],
            'coef': [0.1, 0.2, 0.3]
        })
        mock_read_csv.return_value = mock_cpgs

        # Initialize the clock
        clock = LinClock()

        # Assert that the CSV file was read correctly
        mock_read_csv.assert_called_once_with('data/CpGs/Lin_CpGs.csv')

        # Assert that the attributes are set correctly
        self.assertEqual(clock.name, ClockType.LIN)
        self.assertEqual(clock.marker_name, 'id')
        self.assertEqual(clock.coef_name, 'coef')
        self.assertEqual(clock.reg_coef, 12.2169841)
        pd.testing.assert_frame_equal(clock.cpgs, mock_cpgs)

    @patch('pandas.read_csv')
    def test_initialization_csv_missing(self, mock_read_csv):
        """Test initialization when the CSV file is missing."""
        # Simulate a FileNotFoundError
        mock_read_csv.side_effect = FileNotFoundError

        with self.assertRaises(FileNotFoundError):
            LinClock()


if __name__ == '__main__':
    unittest.main()
