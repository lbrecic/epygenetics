from epygenetics.store.store import AbstractDataStore
from epygenetics.store.strategies.csv import CSVDataStore
from epygenetics.store.strategies.database import DatabaseDataStore


class DataStoreFactory:
    """Factory class to create instances of data stores."""

    @staticmethod
    def create_data_store(store_type: str, path: str) -> AbstractDataStore:
        """
        Factory method to create a data store instance.

        Args:
            store_type (str): The type of data store ('database' or 'csv').
            path (str): The path to the database file or directory containing CSV files.

        Returns:
            AbstractDataStore: An instance of a concrete data store.

        Raises:
            ValueError: If an unknown data store type is specified.
        """
        if store_type == 'database':
            return DatabaseDataStore(db_path=path)
        elif store_type == 'csv':
            return CSVDataStore(directory_path=path)
        else:
            raise ValueError(f"Unknown data store type: {store_type}")
