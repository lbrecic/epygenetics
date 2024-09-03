import pandas as pd

from epygenetics.loader.loader import AbstractLoader


class CSVLoader(AbstractLoader):
    """
    Concrete implementation of AbstractLoader for loading data from a CSV file.
    """

    def load_data(self, file_path: str) -> pd.DataFrame:
        """
        Load data from a CSV file.

        Args:
            file_path (str): The path to the CSV file.

        Returns:
            pd.DataFrame: A pandas DataFrame containing the loaded data.

        Raises:
            FileNotFoundError: If the specified CSV file does not exist.
            pd.errors.EmptyDataError: If the CSV file is empty.
            pd.errors.ParserError: If the CSV file cannot be parsed.
        """
        try:
            df = pd.read_csv(file_path)
        except FileNotFoundError as e:
            raise FileNotFoundError(f"The specified CSV file does not exist: {file_path}") from e
        except pd.errors.EmptyDataError as e:
            raise pd.errors.EmptyDataError(f"The CSV file is empty: {file_path}") from e
        except pd.errors.ParserError as e:
            raise pd.errors.ParserError(f"Error parsing the CSV file: {file_path}") from e

        return df
