from typing import List

import pandas as pd


def subset_cg(dat: pd.DataFrame, cg_set: List[str]) -> pd.DataFrame:
    """
    A function to quickly subset the CpGs you want to work with in a methylation dataframe.

    Parameters:
    dat : DataFrame
        The methylation Beta values you will need to subset, where columns are CpGs (and are named), and rows are samples.
    cg_set : List[str]
        The character vector of Illumina CpG probe IDs that you will be subsetting to.

    Returns:
    DataFrame
        A new beta methylation matrix with columns of only the CpGs that you wanted to subset to.
    """
    match1 = dat.columns.isin(cg_set)
    if not match1.any():
        missing_cpgs = len(cg_set) - match1.sum()
        print(f"{missing_cpgs} CpGs in the requested subset are missing from your data.")

    dat_reduced = dat.loc[:, match1]
    return dat_reduced

# Example usage:
# example_betas = pd.read_csv('exampleBetas.csv')
# horvath_online_ref = pd.read_csv('HorvathOnlineRef.csv')
# result = subset_cg(example_betas, horvath_online_ref['Name'].tolist())
