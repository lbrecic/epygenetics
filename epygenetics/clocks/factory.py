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
from epygenetics.clocks.chronological_age_predictors.lin import LinClock
from epygenetics.clocks.chronological_age_predictors.weidner import WeidnerClock
from epygenetics.clocks.chronological_age_predictors.vidal_bralo import \
    VidalBraloClock
from epygenetics.clocks.chronological_age_predictors.zhang import ZhangClock
from epygenetics.clocks.type import ClockType
from epygenetics.clocks.gestational_and_pediatric_age_predictors.bohlin import \
    BohlinClock
from epygenetics.clocks.gestational_and_pediatric_age_predictors.knight import \
    KnightClock
from epygenetics.clocks.gestational_and_pediatric_age_predictors.lee_control import \
    LeeControlClock
from epygenetics.clocks.gestational_and_pediatric_age_predictors.lee_robust import \
    LeeRobustClock
from epygenetics.clocks.gestational_and_pediatric_age_predictors.lee_refined_robust import \
    LeeRefinedRobustClock
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
from epygenetics.clocks.chronological_age_predictors.hannum import HannumClock
from epygenetics.clocks.trait_predictors.smoking_mccartney import \
    SmokingMcCartneyClock
from epygenetics.clocks.base_clocks.clock import Clock


class ClockFactory:
    def create_clock(self, clock_type: ClockType) -> Clock:
        if clock_type == ClockType.HRS_IN_CH_PHENO_AGE:
            return HRSInCHPhenoAgeClock()
        elif clock_type == ClockType.NON_PRC_PHENO_AGE:
            return NonPRCPhenoAgeClock()
        elif clock_type == ClockType.PHENO_AGE:
            return PhenoAgeClock()
        elif clock_type == ClockType.PRC_PHENO_AGE:
            return PRCPhenoAgeClock()
        elif clock_type == ClockType.EPITOC:
            return EpiTOCClock()
        elif clock_type == ClockType.EPITOC2:
            return EpiTOC2Clock
        elif clock_type == ClockType.HYPO_CLOCK:
            return HypoClock()
        elif clock_type == ClockType.MIAGE:
            return MiAgeClock()
        elif clock_type == ClockType.BOCKLANDT:
            return BocklandtClock()
        elif clock_type == ClockType.GARAGNANI:
            return GaragnaniClock()
        elif clock_type == ClockType.HANNUM:
            return HannumClock()
        elif clock_type == ClockType.HORVATH_MULTITISSUE:
            return HorvathMultitissueClock()
        elif clock_type == ClockType.LIN:
            return LinClock()
        elif clock_type == ClockType.VIDAL_BRALO:
            return VidalBraloClock()
        elif clock_type == ClockType.WEIDNER:
            return WeidnerClock()
        elif clock_type == ClockType.ZHANG:
            return ZhangClock()
        elif clock_type == ClockType.BOHLIN:
            return BohlinClock()
        elif clock_type == ClockType.KNIGHT:
            return KnightClock()
        elif clock_type == ClockType.LEE_CONTROL:
            return LeeControlClock()
        elif clock_type == ClockType.LEE_REFINED_ROBUST:
            return LeeRefinedRobustClock()
        elif clock_type == ClockType.LEE_ROBUST:
            return LeeRobustClock()
        elif clock_type == ClockType.MAYNE:
            return MayneClock()
        elif clock_type == ClockType.PEDBE:
            return PEDBEClock()
        elif clock_type == ClockType.DNAM_AGE_CORTICAL:
            return DNAmAgeCorticalClock()
        elif clock_type == ClockType.HORVATH_SKIN_AND_BLOOD:
            return HorvathSkinAndBloodClock()
        elif clock_type == ClockType.ALCOHOL_MCCARTNEY:
            return AlcoholMcCartneyClock()
        elif clock_type == ClockType.BMI_MCCARTNEY:
            return BMIMcCartneyClock()
        elif clock_type == ClockType.SMOKING_MCCARTNEY:
            return SmokingMcCartneyClock()
        else:
            print('Provided clock type is not recognized. Please choose from the following list:')
            ClockType.list_predefined_clocks()
            raise ValueError(f"Clock type {clock_type} not recognized")
