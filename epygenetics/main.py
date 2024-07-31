import pandas as pd

from clocks.chronological_age_predictors.horvath_multitissue import HorvathMultitissueClock

betas = pd.read_csv('../data/examples/exampleBetas.csv')
pheno = pd.read_csv('../data/examples/examplePheno.csv')

# print("PhenoAge Clock:")
# PhenoAgeClock().execute(betas, pheno)
# print("###################################################")
#
# print("PRCPhenoAge Clock:")
# PRCPhenoAgeClock().execute(betas, pheno)
# print("###################################################")

print("Horvath Clock:")
HorvathMultitissueClock().execute(betas)
print("###################################################")
