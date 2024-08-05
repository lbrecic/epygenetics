from enum import StrEnum


class ClockType(StrEnum):
    HRS_IN_CH_PHENO_AGE = 'HRSInChPhenoAge'
    NON_PRC_PHENO_AGE = 'non_prcPhenoAge'
    PRC_PHENO_AGE = 'prcPhenoAge'
    PHENO_AGE = 'PhenoAge'
    EPITOC = 'EpiTOC'
    EPITOC2 = 'EpiTOC2'
    HYPO_CLOCK = 'hypoClock'
    MIAGE = 'MiAge'
    BOCKLANDT = 'Bocklandt'
    GARAGNANI = 'Garagnani'
    HANNUM = 'Hannum'
    HORVATH_MULTITISSUE = 'Horvath1'
    LIN = 'Lin'
    VIDAL_BRALO = 'VidalBralo'
    WEIDNER = 'Weidner'
    ZHANG = 'Zhang'
    BOHLIN = 'Bohlin'
    KNIGHT = 'Knight'
    LEE_CONTROL = 'LeeControl'
    LEE_ROBUST = 'LeeRobust'
    LEE_REFINED_ROBUST = 'LeeRefinedRobust'
    MAYNE = 'Mayne'
    PEDBE = 'PEDBE'
    DNAM_AGE_CORTICAL = 'DNAmClockCortical'
    HORVATH_SKIN_AND_BLOOD = 'Horvath2'
    ALCOHOL_MCCARTNEY = 'Alcohol_McCartney'
    BMI_MCCARTNEY = 'BMI_McCartney'
    SMOKING_MCCARTNEY = 'Smoking_McCartney'


def list_predefined_clocks() -> None:
    [print(e.value) for e in ClockType]
