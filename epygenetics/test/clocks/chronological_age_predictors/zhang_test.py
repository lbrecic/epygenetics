import unittest
from unittest.mock import patch
import pandas as pd

from epygenetics.clocks.chronological_age_predictors.zhang import ZhangClock
from epygenetics.clocks.type import ClockType


class ZhangClockTestCase(unittest.TestCase):

    @patch('pandas.read_csv')
    def test_initialization(self, mock_read_csv):
        """Test the initialization of ZhangClock."""
        # Mock the CpG DataFrame
        mock_cpgs = pd.DataFrame({
            'Marker': ['cg00000029', 'cg00000108', 'cg00000109'],
            'coef': [0.1, 0.2, 0.3]
        })
        mock_read_csv.return_value = mock_cpgs

        # Initialize the clock
        clock = ZhangClock()

        # Assert that the CSV file was read correctly
        mock_read_csv.assert_called_once_with('data/CpGs/Zhang_10_CpG.csv')

        # Assert that the attributes are set correctly
        self.assertEqual(clock.name, ClockType.ZHANG)
        self.assertEqual(clock.marker_name, 'Marker')
        self.assertEqual(clock.coef_name, 'coef')
        self.assertEqual(clock.reg_coef, 0)
        pd.testing.assert_frame_equal(clock.cpgs, mock_cpgs)

    @patch('pandas.read_csv')
    def test_initialization_csv_missing(self, mock_read_csv):
        """Test initialization when the CSV file is missing."""
        # Simulate a FileNotFoundError
        mock_read_csv.side_effect = FileNotFoundError

        with self.assertRaises(FileNotFoundError):
            ZhangClock()


if __name__ == '__main__':
    unittest.main()
