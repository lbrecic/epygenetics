from enum import StrEnum


class ImputerType(StrEnum):
    KNN = 'knn'
    MEAN = 'mean'
    MEDIAN = 'median'
    MICE = 'mice'
    REGULAR = 'regular'

    @staticmethod
    def from_str(label: str) -> 'ImputerType':
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
            raise ValueError(f"Invalid imputer type: {label}")

    @staticmethod
    def list_available_imputers() -> None:
        [print(e.value) for e in ImputerType]
