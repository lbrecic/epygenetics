from abc import ABC, abstractmethod

import pandas as pd


class AbstractDataStore(ABC):
    """Abstract base class for a data store used to retrieve DNA methylation data for epigenetic clocks."""

    @abstractmethod
    def retrieve_methylation_data(self, clock_name: str) -> pd.DataFrame:
        """
        Retrieve DNA methylation data for a specific epigenetic clock.

        Args:
            clock_name (str): The name of the epigenetic clock for which to retrieve data.

        Returns:
            pd.DataFrame: A pandas DataFrame containing the methylation data.
        """
        pass
