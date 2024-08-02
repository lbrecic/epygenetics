import pandas as pd

from epygenetics.clocks.base_clocks.regression_clock import RegressionClock
from epygenetics.clocks.biological_age_and_mortality_predictors.pheno_age import \
    PhenoAgeClock
from epygenetics.clocks.biological_age_and_mortality_predictors.prc_pheno_age import \
    PRCPhenoAgeClock
from epygenetics.clocks.chronological_age_predictors import \
    HorvathMultitissueClock


class TestClock(RegressionClock):
    def __init__(self):
        cpgs = pd.read_csv('data/CpGs/PhenoAge_CpGs.csv')
        super().__init__('Test', cpgs, 'CpG', 'Weight', 0)


def main():
    betas = pd.read_csv('data/examples/exampleBetas.csv')
    pheno = pd.read_csv('data/examples/examplePheno.csv')

    print("PhenoAge Clock:")
    PhenoAgeClock().execute(betas, pheno)
    print("###################################################")

    print("PRCPhenoAge Clock:")
    PRCPhenoAgeClock().execute(betas, pheno)
    print("###################################################")

    print("Horvath Clock:")
    HorvathMultitissueClock().execute(betas)
    print("###################################################")

    TestClock().execute(betas, pheno)
    print("###################################################")


if __name__ == '__main__':
    main()
