from typing import Optional

import pandas as pd

from epygenetics.imputers.strategies.knn import KNNImputer
from epygenetics.imputers.strategies.mean import MeanImputer
from epygenetics.imputers.strategies.regular import RegularImputer
from epygenetics.imputers.strategies.median import MedianImputer
from epygenetics.imputers.strategies.mice import MICEImputer
from epygenetics.imputers.base_imputer import BaseImputer
from epygenetics.imputers.type import ImputerType


class ImputerFactory:
    @staticmethod
    def create_imputer(imputer_type: ImputerType, cpg_imputation: Optional[pd.DataFrame] = None) -> BaseImputer:
        if imputer_type == ImputerType.KNN:
            return KNNImputer()
        elif imputer_type == ImputerType.MICE:
            return MICEImputer()
        elif imputer_type == ImputerType.MEDIAN:
            return MedianImputer()
        elif imputer_type == ImputerType.MEAN:
            return MeanImputer()
        elif imputer_type == ImputerType.REGULAR:
            return RegularImputer(cpg_imputation)
        else:
            print('Provided imputer type is not recognized. Please choose from the following list:')
            ImputerType.list_available_imputers()
            raise ValueError(f"Imputer type {imputer_type} not recognized")