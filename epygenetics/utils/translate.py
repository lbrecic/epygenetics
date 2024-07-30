import os.path

import pandas as pd
import pyreadr

cpgs_names = ['Alcohol_CpGs', 'BMI_CpGs', 'Bocklandt_CpG', 'Bohlin_CpGs', 'DNAmClockCortical_CpGs', 'DNAmTL_CpGs','EpiToc2_CpGs', 'EpiToc_CpGs', 'Garagnani_CpG', 'Hannum_CpGs','Horvath1_CpGs', 'Horvath2_CpGs', 'HorvathOnlineRef','HRSInCHPhenoAge_CpGs', 'hypoClock_CpGs', 'Knight_CpGs','LeeControl_CpGs', 'LeeRefinedRobust_CpGs', 'LeeRobust_CpGs','Lin_CpGs', 'Mayne_CpGs', 'MiAge_CpGs', 'PEDBE_CpGs','PhenoAge_CpGs', 'Smoking_CpGs', 'VidalBralo_CpGs','Weidner_CpGs', 'Zhang2019_CpGs', 'Zhang_10_CpG']
imputes_names = ['DNAmClockCortical_imputeRef', 'Mayne_impute']
example_names = ['exampleBetas', 'examplePheno', 'HorvathOnlineRef']
parameters_names = ['MiAge_parameters']
other_names = ['prcPhenoAge', 'non_prcPhenoAge', 'exampleBetas', 'examplePheno']


cpgs_output_path = '../../data/CpGs/'
imputes_output_path = '../../data/imputes/'
examples_output_path = '../../data/examples/'
params_output_path = '../../data/params/'
other_output_path = '../../data/other/'

files = [(other_names, other_output_path)]
# (cpgs_names, cpgs_output_path), (imputes_names, imputes_output_path), (example_names, examples_output_path), (parameters_names, params_output_path),

for names, output_path in files:
    if os.path.exists(output_path) == False:
        os.mkdir(output_path)

    for name in names:
        cpgs_dict = pyreadr.read_r(f'data/{name}.rda')
        print(cpgs_dict)
        cpgs = pd.DataFrame(cpgs_dict[name])
        cpgs.to_csv(f'{output_path}{name}.csv', index=False)
        print(f'{name} done')

