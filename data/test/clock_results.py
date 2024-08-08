import numpy as np
import pandas as pd

from epygenetics.clocks.type import ClockType

methylCIPHER = pd.DataFrame({
    ClockType.HRS_IN_CH_PHENO_AGE: [55.52177, 5512549, 55.58441, 55.67962, 55.72232],
    ClockType.PHENO_AGE: [52.29315, 41.05867, 43.54460, 43.96697, 40.35242],
    ClockType.EPITOC: [0.12408041, 0.11472045, 0.08814333, 0.09467855, 0.09366637],
    ClockType.HYPO_CLOCK: [0.8443867, 0.8587854, 0.8659912, 0.8669189, 0.8714039],
    ClockType.MIAGE: [276.9358, 649.4476, 255.3803, 275.4913, 296.3778],
    ClockType.BOCKLANDT: [0.4828566, 0.4522614, 0.4768421, 0.5494463, 0.4657794],
    ClockType.GARAGNANI: [0.6951288, 0.6102083, 0.5848794, 0.5969861, 0.6506833],
    ClockType.HANNUM: [62.33422, 53.90139, 53.59733, 59.53767, 58.80107],
    ClockType.HORVATH_MULTITISSUE: [56.20544, 47.45754, 48.24172, 51.53588, 45.05448],
    ClockType.LIN: [47.46955, 36.32625, 26.39302, 31.48122, 32.54199],
    ClockType.VIDAL_BRALO: [27.17847, 28.71482, 28.46388, 29.35216, 28.32386],
    ClockType.WEIDNER: [107.39252, 126.26082, 48.26884, 104.53928, 118.65014],
    ClockType.ZHANG: [-3.013470, -2.867893, -2.942713, -3.260276, -2.936251],
    ClockType.BOHLIN: [290.5586, 289.3656, 289.7912, 289.3616, 289.8215],
    ClockType.KNIGHT: [43.75382, 43.18014, 43.41194, 43.26718, 43.36476],
    ClockType.LEE_CONTROL: [12.14854, 12.16179, 12.01177, 12.04271, 11.96609],
    ClockType.LEE_ROBUST: [24.95762, 24.96283, 24.87859, 24.93005, 24.92568],
    ClockType.LEE_REFINED_ROBUST: [30.02084, 30.02200, 29.96719, 30.03654, 30.08753],
    ClockType.MAYNE: [18.81865, 19.31211, 19.11796, 19.33233, 19.58006],
    ClockType.PEDBE: [8.667792, 7.397710, 6.868020, 7.210960, 7.287029],
    ClockType.DNAM_AGE_CORTICAL: [51.11870, 47.19439, 46.44424, 48.66254, 47.35857],
    ClockType.HORVATH_SKIN_AND_BLOOD: [58.70330, 51.05889, 50.36209, 54.37485, 54.07953],
    # ClockType.ALCOHOL_MCCARTNEY: [-11.77366, -11.77065, -12.14878, -12.21418, -12.22958],
    # ClockType.BMI_MCCARTNEY: [-0.3433347, -0.6141560, -0.6782138, -0.3257721, -0.5696143],
    # ClockType.SMOKING_MCCARTNEY: [3.993508, 4.501657, 3.173744, 3.216788, 4.414541],
})

epygenetics = pd.DataFrame({
    ClockType.HRS_IN_CH_PHENO_AGE: [46.175572, 40.475084, 45.658330, 49.907506, 48.901753],
    ClockType.PHENO_AGE: [52.293152, 41.058674, 43.544603, 43.966974, np.nan],
    ClockType.EPITOC: [0.124080, 0.114720, 0.088143, 0.094679, 0.093666],
    ClockType.HYPO_CLOCK: [0.844387, 0.858785, 0.865991, 0.866919, 0.871404],
    ClockType.MIAGE: [np.nan, np.nan, np.nan, np.nan, np.nan],  # Not working
    ClockType.BOCKLANDT: [0.482857, 0.452261, 0.476842, 0.549446, 0.465779],
    ClockType.GARAGNANI: [0.695129, 0.610208, 0.584879, 0.596986, 0.650683],
    ClockType.HANNUM: [62.334222, 53.901388, 53.597325, 59.537669, 58.801074],
    ClockType.HORVATH_MULTITISSUE: [56.205439, 47.457539, 48.241724, 51.535883, 45.054478],
    ClockType.LIN: [45.585684, 34.323300, 24.506547, 29.620897, 30.734696],  # KNN imputation
    ClockType.VIDAL_BRALO: [50.518861, 53.530620, 51.836565, 52.400827, 50.715486],  # KNN imputation
    ClockType.WEIDNER: [58.265374, 54.144983, 53.667892, 62.243928, 50.704644],
    ClockType.ZHANG: [-3.013470, -2.867893, -2.942713, -3.260276, -2.936251],
    ClockType.BOHLIN: [292.193728, 291.000691, 291.426289, 290.996663, 291.456610],  # Regular imputation usim sesame_450k_median.csv data
    ClockType.KNIGHT: [46.462954, 45.889277, 46.121079, 45.976312, 46.073900],  # Regular imputation usim sesame_450k_median.csv data
    ClockType.LEE_CONTROL: [18.261555, 18.661235, 18.133249, 18.079320, 17.830622],  # KNN imputation
    ClockType.LEE_ROBUST: [23.612459, 23.532638, 23.531571, 23.601707, 23.635202],  # KNN imputation
    ClockType.LEE_REFINED_ROBUST: [33.049577, 33.242190, 33.000116, 33.027419, 32.993148],  # KNN imputation
    ClockType.MAYNE: [11.703282, 11.746959, 11.992752, 12.305900, 12.753932],  # KNN imputation
    ClockType.PEDBE: [6.337964, 5.263821, 4.969639, 5.253728, 5.360848],  # KNN imputation
    ClockType.DNAM_AGE_CORTICAL: [43.764001, 39.839688, 39.089534, 41.307839, 40.003865],  # Regular imputation usim sesame_450k_median.csv data
    ClockType.HORVATH_SKIN_AND_BLOOD: [57.080572, 49.333591, 48.737121, 52.772401, 52.522762],  # KNN imputation
    # ClockType.ALCOHOL_MCCARTNEY: [],  # Not working completely -> bug
    # ClockType.BMI_MCCARTNEY: [],  # Not working completely -> bug
    # ClockType.SMOKING_MCCARTNEY: [],  # Not working completely -> bug
})

methylCIPHER_prcPhenoAge_data = pd.DataFrame({
    'name': ['7786915023_R02C02', '7786915135_R04C02', '7471147149_R06C01', '7786915035_R05C01', '7786923035_R01C01'],
    'geo_accession': ['GSM1343050', 'GSM1343051', 'GSM1343052', 'GSM1343053', 'GSM1343054'],
    'gender': ['M', 'M', 'M', 'M', 'M'],
    'age': [57.9, 42.0, 47.4, 49.3, 52.5],
    'group': [1.0, 1.0, 1.0, 1.0, 1.0],
    'sample': [1.0, 2.0, 3.0, 4.0, 5.0],
    'prcPhenoAge': [18.60933, 15.03647, 17.92249, 16.86863, 17.00389],
})

epygenetics_prcPhenoAge_data = pd.DataFrame({
    'name': ['7786915023_R02C02', '7786915135_R04C02', '7471147149_R06C01', '7786915035_R05C01', '7786923035_R01C01'],
    'geo_accession': ['GSM1343050', 'GSM1343051', 'GSM1343052', 'GSM1343053', 'GSM1343054'],
    'gender': ['M', 'M', 'M', 'M', 'M'],
    'age': [57.9, 42.0, 47.4, 49.3, 52.5],
    'group': [1.0, 1.0, 1.0, 1.0, 1.0],
    'sample': [1.0, 2.0, 3.0, 4.0, 5.0],
    'prcPhenoAge': [18.609329, 15.036468, 17.922490, 16.868625, 17.003892],
})

methylCIPHER_nonPrcPhenoAge_data = pd.DataFrame({
    'name': ['7786915023_R02C02', '7786915135_R04C02', '7471147149_R06C01', '7786915035_R05C01', '7786923035_R01C01'],
    'geo_accession': ['GSM1343050', 'GSM1343051', 'GSM1343052', 'GSM1343053', 'GSM1343054'],
    'gender': ['M', 'M', 'M', 'M', 'M'],
    'age': [57.9, 42.0, 47.4, 49.3, 52.5],
    'group': [1.0, 1.0, 1.0, 1.0, 1.0],
    'sample': [1.0, 2.0, 3.0, 4.0, 5.0],
    'non_prcPhenoAge': [-26.98018, -34.64179, -35.04189, -33.56565, -37.31548],
})

epygenetics_nonPrcPhenoAge_data = pd.DataFrame({
    'name': ['7786915023_R02C02', '7786915135_R04C02', '7471147149_R06C01', '7786915035_R05C01', '7786923035_R01C01'],
    'geo_accession': ['GSM1343050', 'GSM1343051', 'GSM1343052', 'GSM1343053', 'GSM1343054'],
    'gender': ['M', 'M', 'M', 'M', 'M'],
    'age': [57.9, 42.0, 47.4, 49.3, 52.5],
    'group': [1.0, 1.0, 1.0, 1.0, 1.0],
    'sample': [1.0, 2.0, 3.0, 4.0, 5.0],
    'non_prcPhenoAge': [-26.980177, -34.641793, -35.041887, -33.565651, np.nan],
})
