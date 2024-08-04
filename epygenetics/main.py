import pandas as pd

from epygenetics.clocks.base_clocks.regression_clock import RegressionClock
from epygenetics.clocks.biological_age_and_mortality_predictors.hrs_in_ch_pheno_age import \
    HRSInCHPhenoAgeClock
from epygenetics.clocks.biological_age_and_mortality_predictors.non_prc_pheno_age import \
    NonPRCPhenoAgeClock
from epygenetics.clocks.biological_age_and_mortality_predictors.pheno_age import \
    PhenoAgeClock
from epygenetics.clocks.biological_age_and_mortality_predictors.prc_pheno_age import \
    PRCPhenoAgeClock
from epygenetics.clocks.cancer_and_mitotic_rates_predictors.epitoc import \
    EpiTOCClock
from epygenetics.clocks.cancer_and_mitotic_rates_predictors.epitoc2 import \
    EpiTOC2Clock
from epygenetics.clocks.cancer_and_mitotic_rates_predictors.hypo_clock import \
    HypoClock
from epygenetics.clocks.cancer_and_mitotic_rates_predictors.miage import \
    MiAgeClock
from epygenetics.clocks.chronological_age_predictors import \
    HorvathMultitissueClock
from epygenetics.clocks.chronological_age_predictors.bocklandt import \
    BocklandtClock
from epygenetics.clocks.chronological_age_predictors.garagnani import \
    GaragnaniClock
from epygenetics.clocks.chronological_age_predictors.hannum import HannumClock
from epygenetics.clocks.chronological_age_predictors.zhang import ZhangClock
from epygenetics.clocks.gestational_and_pediatric_age_predictors.bohlin import \
    BohlinClock
from epygenetics.clocks.gestational_and_pediatric_age_predictors.knight import \
    KnightClock
from epygenetics.clocks.gestational_and_pediatric_age_predictors.lee_control import \
    LeeControlClock
from epygenetics.clocks.gestational_and_pediatric_age_predictors.mayne import \
    MayneClock
from epygenetics.clocks.gestational_and_pediatric_age_predictors.pedbe import \
    PEDBEClock
from epygenetics.clocks.non_blood_clocks.dna_m_age_cortical import \
    DNAmAgeCorticalClock
from epygenetics.clocks.non_blood_clocks.horvath_skin_and_blood import \
    HorvathSkinAndBloodClock
from epygenetics.clocks.trait_predictors.alcohol_mccartney import \
    AlcoholMcCartneyClock
from epygenetics.clocks.trait_predictors.bmi_mccartney import BMIMcCartneyClock
from epygenetics.clocks.trait_predictors.smoking_mccartney import \
    SmokingMcCartneyClock


class TestClock(RegressionClock):
    def __init__(self):
        cpgs = pd.read_csv('data/CpGs/PhenoAge_CpGs.csv')
        super().__init__('Test', 'CpG', 'Weight', 0, cpgs)


def main():
    betas = pd.read_csv('data/examples/exampleBetas.csv')
    pheno = pd.read_csv('data/examples/examplePheno.csv')

    # print("Horvath Clock:")
    # HorvathMultitissueClock().execute(betas)
    # print("###################################################")

    # TestClock().execute(betas, pheno)
    # print("###################################################")

    # print("Garagnani Clock:")
    # GaragnaniClock().execute(betas)
    # print("###################################################")
    #
    # print("Hannum Clock:")
    # HannumClock().execute(betas)
    # print("###################################################")
    #
    # print("Zhang Clock:")
    # ZhangClock().execute(betas)
    # print("###################################################")

    # print("Bohlin Clock:")
    # BohlinClock().execute(betas)
    # print("###################################################")

    # print("Knight Clock:")
    # KnightClock().execute(betas)
    # print("###################################################")

    # print("Lee Control Clock:")
    # LeeControlClock().execute(betas)
    # print("###################################################")

    imputation = pd.read_csv('data/imputes/Mayne_impute.csv')
    print("Mayne Clock:")
    MayneClock().execute(betas, None, imputation, True)
    # MayneClock().execute(betas, None, None, True)
    print("###################################################")

    # print("Alcohol McCartney Clock:")
    # AlcoholMcCartneyClock().execute(betas)
    # print("###################################################")

    # print("BMI McCartney Clock:")
    # BMIMcCartneyClock().execute(betas)
    # print("###################################################")

    # print("Smoking McCartney Clock:")
    # SmokingMcCartneyClock().execute(betas)
    # print("###################################################")

    # print("Horvath Skin and Blood Clock:")
    # HorvathSkinAndBloodClock().execute(betas)
    # print("###################################################")

    # imputation = pd.read_csv('data/imputes/DNAmClockCortical_imputeRef.csv')
    # print("DNAm Age Cortical Clock:")
    # DNAmAgeCorticalClock().execute(betas, None, imputation, True)
    # print("###################################################")

    # print("Bocklandt Clock:")
    # BocklandtClock().execute(betas)
    # print("###################################################")
    #
    # print("EpiTOC Clock:")
    # EpiTOCClock().execute(betas)
    # print("###################################################")
    #
    # print("Hypo Clock:")
    # HypoClock().execute(betas)
    # print("###################################################")
    #
    # imputation = pd.read_csv('data/imputes/Mayne_impute.csv')
    # print("MiAge Clock:")
    # MiAgeClock(1.4, 2.2, 0.2).execute(betas, None, imputation, True)
    # print("###################################################")

    # print("EpiTOC2 Clock:")
    # EpiTOC2Clock().execute(betas)
    # print("###################################################")

    # print("PhenoAge Clock:")
    # PhenoAgeClock().execute(betas)
    # print("###################################################")
    #
    # print("PRCPhenoAge Clock:")
    # PRCPhenoAgeClock().execute(betas)
    # print("###################################################")
    #
    # print("Non PRCPhenoAge Clock:")
    # NonPRCPhenoAgeClock().execute(betas)
    # print("###################################################")

    # print("HRS In CH Pheno Age Clock:")
    # HRSInCHPhenoAgeClock().execute(betas)
    # print("###################################################")

    # print("PEDBE Clock:")
    # PEDBEClock().execute(betas)
    # print("###################################################")


if __name__ == '__main__':
    main()
