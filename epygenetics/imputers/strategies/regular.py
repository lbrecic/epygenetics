from typing import Optional

import pandas as pd

from epygenetics.imputers.base_imputer import BaseImputer


class RegularImputer(BaseImputer):
    def __init__(self, cpg_imputation: Optional[pd.DataFrame]) -> None:
        self.cpg_imputation: Optional[pd.DataFrame] = cpg_imputation

    def impute(self, dna_m: pd.DataFrame) -> pd.DataFrame:
        if not isinstance(dna_m, pd.DataFrame) or not isinstance(self.cpg_imputation, pd.DataFrame):
            raise ValueError("Inputs must be a pandas DataFrame")

        for cpg in dna_m.columns:
            if dna_m[cpg].isna().all():
                headers = self.cpg_imputation.columns.tolist()
                dna_m[cpg] = self.cpg_imputation[self.cpg_imputation[headers[0]] == cpg][headers[1]].values[0]

        return dna_m
