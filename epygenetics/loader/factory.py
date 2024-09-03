from epygenetics.loader.loader import AbstractLoader
from epygenetics.loader.strategies.csv import CSVLoader
from epygenetics.loader.strategies.rda import RDALoader


class LoaderFactory:
    """
    Factory class to create instances of data loaders.
    """

    @staticmethod
    def create_loader(loader_type: str) -> AbstractLoader:
        """
        Factory method to create a loader instance.

        Args:
            loader_type (str): The type of loader ('csv', 'rda', etc.).

        Returns:
            AbstractLoader: An instance of a concrete loader.

        Raises:
            ValueError: If an unknown loader type is specified.
        """
        if loader_type == 'csv':
            return CSVLoader()
        elif loader_type == 'rda':
            return RDALoader()
        else:
            raise ValueError(f"Unknown loader type: {loader_type}")
