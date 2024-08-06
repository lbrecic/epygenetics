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

    @staticmethod
    def from_str(label: str) -> 'ClockType':
        if label == 'HRSInChPhenoAge':
            return ClockType.HRS_IN_CH_PHENO_AGE
        elif label == 'non_prcPhenoAge':
            return ClockType.NON_PRC_PHENO_AGE
        elif label == 'prcPhenoAge':
            return ClockType.PRC_PHENO_AGE
        elif label == 'PhenoAge':
            return ClockType.PHENO_AGE
        elif label == 'EpiTOC':
            return ClockType.EPITOC
        elif label == 'EpiTOC2':
            return ClockType.EPITOC2
        elif label == 'hypoClock':
            return ClockType.HYPO_CLOCK
        elif label == 'MiAge':
            return ClockType.MIAGE
        elif label == 'Bocklandt':
            return ClockType.BOCKLANDT
        elif label == 'Garagnani':
            return ClockType.GARAGNANI
        elif label == 'Hannum':
            return ClockType.HANNUM
        elif label == 'Horvath1':
            return ClockType.HORVATH_MULTITISSUE
        elif label == 'Lin':
            return ClockType.LIN
        elif label == 'VidalBralo':
            return ClockType.VIDAL_BRALO
        elif label == 'Weidner':
            return ClockType.WEIDNER
        elif label == 'Zhang':
            return ClockType.ZHANG
        elif label == 'Bohlin':
            return ClockType.BOHLIN
        elif label == 'Knight':
            return ClockType.KNIGHT
        elif label == 'LeeControl':
            return ClockType.LEE_CONTROL
        elif label == 'LeeRobust':
            return ClockType.LEE_ROBUST
        elif label == 'LeeRefinedRobust':
            return ClockType.LEE_REFINED_ROBUST
        elif label == 'Mayne':
            return ClockType.MAYNE
        elif label == 'PEDBE':
            return ClockType.PEDBE
        elif label == 'DNAmClockCortical':
            return ClockType.DNAM_AGE_CORTICAL
        elif label == 'Horvath2':
            return ClockType.HORVATH_SKIN_AND_BLOOD
        elif label == 'Alcohol_McCartney':
            return ClockType.ALCOHOL_MCCARTNEY
        elif label == 'BMI_McCartney':
            return ClockType.BMI_MCCARTNEY
        elif label == 'Smoking_McCartney':
            return ClockType.SMOKING_MCCARTNEY
        else:
            raise NotImplementedError(f"Clock type {label} is not implemented")

    @staticmethod
    def list_predefined_clocks() -> None:
        [print(e.value) for e in ClockType]
