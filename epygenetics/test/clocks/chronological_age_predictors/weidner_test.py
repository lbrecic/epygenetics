import unittest
from unittest.mock import patch
import pandas as pd

from epygenetics.clocks.chronological_age_predictors.weidner import WeidnerClock
from epygenetics.clocks.type import ClockType


class WeidnerClockTestCase(unittest.TestCase):

    @patch('pandas.read_csv')
    def test_initialization(self, mock_read_csv):
        """Test the initialization of WeidnerClock."""
        # Mock the CpG DataFrame
        mock_cpgs = pd.DataFrame({
            'Weidner_CpGs': ['cg00000029', 'cg00000108', 'cg00000109'],
            'Coefficient': [0.1, 0.2, 0.3]
        })
        mock_read_csv.return_value = mock_cpgs

        # Initialize the clock
        clock = WeidnerClock()

        # Assert that the CSV file was read correctly
        mock_read_csv.assert_called_once_with('data/CpGs/Weidner_CpGs.csv')

        # Assert that the attributes are set correctly
        self.assertEqual(clock.name, ClockType.WEIDNER)
        self.assertEqual(clock.marker_name, 'Weidner_CpGs')
        self.assertEqual(clock.coef_name, 'Coefficient')
        self.assertEqual(clock.reg_coef, 111.83)
        pd.testing.assert_frame_equal(clock.cpgs, mock_cpgs)

    @patch('pandas.read_csv')
    def test_initialization_csv_missing(self, mock_read_csv):
        """Test initialization when the CSV file is missing."""
        # Simulate a FileNotFoundError
        mock_read_csv.side_effect = FileNotFoundError

        with self.assertRaises(FileNotFoundError):
            WeidnerClock()


if __name__ == '__main__':
    unittest.main()
