import pandas as pd
from pyreadr import pyreadr

from epygenetics.loader.loader import AbstractLoader


class RDALoader(AbstractLoader):
    """
    Concrete implementation of AbstractLoader for loading data from an R .rda file.
    """

    def load_data(self, file_path: str) -> pd.DataFrame:
        """
        Load data from an R .rda file.

        Args:
            file_path (str): The path to the .rda file.

        Returns:
            pd.DataFrame: A pandas DataFrame containing the loaded data.

        Raises:
            FileNotFoundError: If the specified .rda file does not exist.
            ValueError: If the .rda file does not contain any data frames.
        """
        try:
            result = pyreadr.read_r(file_path)  # this returns a dictionary with all the data frames in the file
        except FileNotFoundError as e:
            raise FileNotFoundError(f"The specified .rda file does not exist: {file_path}") from e
        except Exception as e:
            raise Exception(f"An error occurred while reading the .rda file: {file_path}") from e

        # Extract the first DataFrame found in the .rda file
        if not result:
            raise ValueError(f"The .rda file does not contain any data frames: {file_path}")

        df = next(iter(result.values()))

        if not isinstance(df, pd.DataFrame):
            raise ValueError(f"The .rda file does not contain a valid data frame: {file_path}")

        return df
