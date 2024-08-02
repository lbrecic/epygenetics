from abc import ABC, abstractmethod

import pandas as pd


class Clock(ABC):
    def __init__(self, name, marker_name, cpgs=None):
        self.name = name
        self.marker_name = marker_name
        self.cpgs = cpgs

    def load_cpgs_from_csv(self, path):
        self.cpgs = pd.read_csv(path)

    @abstractmethod
    def check_cpgs(self, dna_m, cpg_imputation, imputation):
        pass

    @abstractmethod
    def calculate(self, common_cpgs, cpg_check, dna_m, pheno, imputation):
        pass

    def execute(self, dna_m, pheno=None, cpg_imputation=None, imputation=False):
        cpgs, cpg_check = self.check_cpgs(dna_m, cpg_imputation, imputation)
        result = self.calculate(cpgs, cpg_check, dna_m, pheno, imputation)
        print(result)
