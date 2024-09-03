import unittest
from unittest.mock import patch

import pandas as pd

from epygenetics.clocks.chronological_age_predictors.bocklandt import \
    BocklandtClock
from epygenetics.clocks.type import ClockType


class BocklandtClockTestCase(unittest.TestCase):

    @patch('pandas.read_csv')
    def test_initialization(self, mock_read_csv):
        """Test the initialization of BocklandtClock."""
        # Mock the CpG DataFrame
        mock_cpgs = pd.DataFrame({
            'Bocklandt_CpG': ['cg00000029', 'cg00000108', 'cg00000109']
        })
        mock_read_csv.return_value = mock_cpgs

        # Initialize the clock
        clock = BocklandtClock()

        # Assert that the CSV file was read correctly
        mock_read_csv.assert_called_once_with('data/CpGs/Bocklandt.csv')

        # Assert that the attributes are set correctly
        self.assertEqual(clock.name, ClockType.BOCKLANDT)
        self.assertEqual(clock.marker_name, 'Bocklandt_CpG')
        pd.testing.assert_frame_equal(clock.cpgs, mock_cpgs)

    @patch('pandas.read_csv')
    def test_initialization_csv_missing(self, mock_read_csv):
        """Test initialization when the CSV file is missing."""
        # Simulate a FileNotFoundError
        mock_read_csv.side_effect = FileNotFoundError

        with self.assertRaises(FileNotFoundError):
            BocklandtClock()


if __name__ == '__main__':
    unittest.main()
