from enum import StrEnum


class ImputerType(StrEnum):
    """
    Enum class representing the different types of imputers used for handling missing data in epigenetic clocks.
    Each imputer type is associated with a specific string identifier.
    """

    KNN = 'knn'
    MEAN = 'mean'
    MEDIAN = 'median'
    MICE = 'mice'
    REGULAR = 'regular'

    @staticmethod
    def from_str(label: str) -> 'ImputerType':
        """
        Converts a string label to its corresponding `ImputerType` enum.

        Parameters:
            label (str): The string label representing the imputer type.

        Returns:
            ImputerType: The corresponding `ImputerType` enum.

        Raises:
            NotImplementedError: If the provided label does not match any known imputer types.
        """
        if label == 'knn':
            return ImputerType.KNN
        elif label == 'mean':
            return ImputerType.MEAN
        elif label == 'median':
            return ImputerType.MEDIAN
        elif label == 'mice':
            return ImputerType.MICE
        elif label == 'regular':
            return ImputerType.REGULAR
        else:
            print('Provided imputer type is not recognized. Please choose from the following list:')
            ImputerType.list_available_imputers()
            raise NotImplementedError(f"Invalid imputer type: {label}")

    @staticmethod
    def list_available_imputers() -> None:
        """
        Prints a list of all available imputer types in the `ImputerType` enum.
        """
        [print(e) for e in ImputerType]
