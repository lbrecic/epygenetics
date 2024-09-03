from typing import Optional, Tuple, Union

import numpy as np
import pandas as pd

from epygenetics.clocks.base_clocks.clock import Clock
from epygenetics.imputers import ImputerType
from epygenetics.imputers.base_imputer import BaseImputer
from epygenetics.imputers.factory import ImputerFactory
from epygenetics.utils.anti_trafo import anti_trafo
from epygenetics.utils.trafo import trafo


class CustomClock(Clock):

    def __init__(self) -> None:
        cpgs: Optional[pd.DataFrame] = pd.read_csv('../data/examples/exampleCpGs.csv')
        self.reg_coef: float = 50.412
        self.coef_name: str = 'Coef'
        super().__init__("CustomClock", 'CpG', cpgs)

    def validate(self,
                 dna_m: pd.DataFrame,
                 is_imputation: bool = False,
                 imputer_type=ImputerType.REGULAR,
                 cpg_imputation: Optional[pd.DataFrame] = None
                 ) -> Tuple[np.ndarray, bool]:
        if self.cpgs is None:
            raise ValueError("CpGs not loaded.")

        present_cpgs: np.ndarray = np.intersect1d(self.cpgs[self.marker_name], dna_m.columns)
        cpg_check: bool = len(self.cpgs[self.marker_name]) == len(present_cpgs)

        if not cpg_check and is_imputation:
            # Impute missing CpG values
            print(f"Imputation of missing CpG Values occurred for {self.name}")
            for cpg in self.cpgs[self.marker_name]:
                if cpg not in dna_m.columns:
                    dna_m[cpg] = np.nan

            imputer: BaseImputer = ImputerFactory.create_imputer(imputer_type, cpg_imputation)
            imputer.impute(dna_m)

            present_cpgs = self.cpgs[self.marker_name].values

        return present_cpgs, cpg_check

    def calculate(self,
                  dna_m: pd.DataFrame,
                  common_cpgs: np.ndarray,
                  cpg_check: bool,
                  pheno: Optional[pd.DataFrame],
                  is_imputation: bool
                  ) -> Union[pd.DataFrame, pd.Series]:
        if cpg_check or is_imputation:
            beta_values: pd.DataFrame = dna_m[common_cpgs]
            coefficients: pd.Series = self.cpgs.set_index(self.marker_name).loc[common_cpgs, self.coef_name]
            tt: np.ndarray = np.dot(beta_values, coefficients) + self.reg_coef
            tt: anti_trafo(trafo(tt))

            if pheno is not None:
                pheno[self.name] = tt
                return pheno
            else:
                return pd.Series(tt, index=dna_m.index)

        else:
            raise Exception("CpG Check failed and imputation is not enabled or feasible.")


def main():
    clock = CustomClock()
    dna_m = pd.read_csv('../data/examples/exampleBetas.csv')
    clock.execute(dna_m)


if __name__ == '__main__':
    main()
