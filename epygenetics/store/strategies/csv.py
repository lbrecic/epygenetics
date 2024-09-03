import os

import pandas as pd

from epygenetics.store.store import AbstractDataStore


class CSVDataStore(AbstractDataStore):
    """
    Concrete implementation of AbstractDataStore for retrieving DNA methylation data from CSV files.

    Attributes:
        directory_path (str): The directory where CSV files are stored.
    """

    def __init__(self, directory_path: str) -> None:
        """
        Initialize the CSV data store with a directory path.

        Args:
            directory_path (str): The directory where CSV files are stored.
        """
        self.directory_path = directory_path

    def retrieve_methylation_data(self, clock_name: str) -> pd.DataFrame:
        """
        Retrieve DNA methylation data from a CSV file.

        Args:
            clock_name (str): The name of the epigenetic clock for which to retrieve data.

        Returns:
            pd.DataFrame: A pandas DataFrame containing the methylation data.

        Raises:
            FileNotFoundError: If the CSV file for the specified clock name does not exist.
        """
        file_path = os.path.join(self.directory_path, f'{clock_name}.csv')
        if not os.path.exists(file_path):
            raise FileNotFoundError(f'No CSV file found for clock: {clock_name}')
        df = pd.read_csv(file_path)
        return df
