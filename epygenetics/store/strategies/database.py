import sqlite3

import pandas as pd

from epygenetics.store.store import AbstractDataStore


class DatabaseDataStore(AbstractDataStore):
    """
    Concrete implementation of AbstractDataStore for retrieving DNA methylation data from a SQLite database.

    Attributes:
        db_path (str): The file path to the SQLite database.
    """

    def __init__(self, db_path: str) -> None:
        """
        Initialize the database data store with a path to the SQLite database.

        Args:
            db_path (str): The file path to the SQLite database.
        """
        self.db_path = db_path

    def retrieve_methylation_data(self, clock_name: str) -> pd.DataFrame:
        """
        Retrieve DNA methylation data from an SQLite database.

        Args:
            clock_name (str): The name of the epigenetic clock for which to retrieve data.

        Returns:
            pd.DataFrame: A pandas DataFrame containing the methylation data.

        Raises:
            sqlite3.DatabaseError: If there is an issue connecting to or querying the database.
        """
        try:
            conn = sqlite3.connect(self.db_path)
            query = "SELECT * FROM methylation_data WHERE clock_name = ?"
            df = pd.read_sql_query(query, conn, params=(clock_name,))
        except sqlite3.DatabaseError as e:
            raise sqlite3.DatabaseError(f'An error occurred while accessing the database: {e}')
        finally:
            conn.close()

        return df
