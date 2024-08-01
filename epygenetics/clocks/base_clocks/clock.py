from abc import ABC, abstractmethod


class Clock(ABC):
    def __init__(self, name, cpgs, marker_name):
        self.name = name
        self.cpgs = cpgs
        self.marker_name = marker_name

    @abstractmethod
    def check_cpgs(self, dna_m, cpg_imputation, imputation):
        pass

    @abstractmethod
    def calculate(self, common_cpgs, cpg_check, dna_m, pheno, imputation):
        pass

# type hints, is available
    def execute(self, dna_m, pheno=None, cpg_imputation=None, imputation=False):
        cpgs, cpg_check = self.check_cpgs(dna_m, cpg_imputation, imputation)
        result = self.calculate(cpgs, cpg_check, dna_m, pheno, imputation)
        print(result)
