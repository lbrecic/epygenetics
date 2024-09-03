from abc import ABC, abstractmethod

import pandas as pd


class AbstractLoader(ABC):
    """
    Abstract base class for a data loader, which loads data for various epigenetic clocks.
    """

    @abstractmethod
    def load_data(self, file_path: str) -> pd.DataFrame:
        """
        Load data from the specified source.

        Args:
            file_path (str): The path to the data source.

        Returns:
            pd.DataFrame: A pandas DataFrame containing the loaded data.
        """
        pass
