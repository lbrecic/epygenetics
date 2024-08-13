from typing import Optional

import pandas as pd

from epygenetics.imputers.base_imputer import BaseImputer
from epygenetics.imputers.strategies.knn import KNNImputer
from epygenetics.imputers.strategies.mean import MeanImputer
from epygenetics.imputers.strategies.median import MedianImputer
from epygenetics.imputers.strategies.mice import MICEImputer
from epygenetics.imputers.strategies.regular import RegularImputer
from epygenetics.imputers.type import ImputerType


class ImputerFactory:
    """
    A factory class responsible for creating instances of different imputers based
    on the specified imputer type. This class serves as a central point to instantiate
    various imputation strategies for handling missing data.
    """

    @staticmethod
    def create_imputer(imputer_type: ImputerType, cpg_imputation: Optional[pd.DataFrame] = None) -> BaseImputer:
        """
        Creates an instance of a specific imputer based on the provided imputer type.

        Parameters:
            imputer_type (ImputerType): The type of the imputer to be created.
            cpg_imputation (Optional[pd.DataFrame]): A DataFrame containing CpG imputation data,
                                                     required for certain imputation strategies like RegularImputer.
                                                     Defaults to None.

        Returns:
            BaseImputer: An instance of the specified imputer type.

        Raises:
            ValueError: If the imputer type is not recognized or if the necessary CpG
                        imputation data is not provided for the RegularImputer.
        """
        if imputer_type == ImputerType.KNN:
            return KNNImputer()
        elif imputer_type == ImputerType.MICE:
            return MICEImputer()
        elif imputer_type == ImputerType.MEDIAN:
            return MedianImputer()
        elif imputer_type == ImputerType.MEAN:
            return MeanImputer()
        elif imputer_type == ImputerType.REGULAR:
            if cpg_imputation is None:
                raise ValueError("Necessary CpG is missing and no imputation data provided!")
            return RegularImputer(cpg_imputation)
        else:
            print('Provided imputer type is not recognized. Please choose from the following list:')
            ImputerType.list_available_imputers()
            raise ValueError(f"Imputer type {imputer_type} not recognized")
