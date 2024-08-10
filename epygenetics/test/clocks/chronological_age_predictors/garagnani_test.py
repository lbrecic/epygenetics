import unittest
from unittest.mock import patch

import pandas as pd

from epygenetics.clocks.chronological_age_predictors.garagnani import \
    GaragnaniClock
from epygenetics.clocks.type import ClockType


class GaragnaniClockTestCase(unittest.TestCase):

    @patch('pandas.read_csv')
    def test_initialization(self, mock_read_csv):
        """Test the initialization of GaragnaniClock."""
        # Mock the CpG DataFrame
        mock_cpgs = pd.DataFrame({
            'Garagnani': ['cg00000029', 'cg00000108', 'cg00000109']
        })
        mock_read_csv.return_value = mock_cpgs

        # Initialize the clock
        clock = GaragnaniClock()

        # Assert that the CSV file was read correctly
        mock_read_csv.assert_called_once_with('data/CpGs/Garagnani_CpG.csv')

        # Assert that the attributes are set correctly
        self.assertEqual(clock.name, ClockType.GARAGNANI)
        self.assertEqual(clock.marker_name, 'Garagnani')
        pd.testing.assert_frame_equal(clock.cpgs, mock_cpgs)

    @patch('pandas.read_csv')
    def test_initialization_csv_missing(self, mock_read_csv):
        """Test initialization when the CSV file is missing."""
        # Simulate a FileNotFoundError
        mock_read_csv.side_effect = FileNotFoundError

        with self.assertRaises(FileNotFoundError):
            GaragnaniClock()


if __name__ == '__main__':
    unittest.main()
