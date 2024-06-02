import pandas as pd
import pyreadr

name = 'MiAge_CpGs'
cpgs_dict = pyreadr.read_r(f'../../CpGs_data/{name}.rda')
cpgs = pd.DataFrame(cpgs_dict[name])
#print(cpgs_dict)
print(cpgs.index)
print(cpgs)


