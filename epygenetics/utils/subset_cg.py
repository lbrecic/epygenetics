from typing import List

import pandas as pd


def subset_cg(dat: pd.DataFrame, cg_set: List[str]) -> pd.DataFrame:
    """
    Subset a methylation DataFrame to include only the specified CpG sites.

    This function filters the columns of a DataFrame, retaining only those columns that
    match the CpG probe IDs provided in `cg_set`. It also prints a message if any of the
    requested CpG sites are missing from the DataFrame.

    Parameters:
        dat (pd.DataFrame): The input DataFrame containing methylation Beta values,
                            where columns are CpGs and rows are samples.
        cg_set (List[str]): A list of Illumina CpG probe IDs to subset the DataFrame.

    Returns:
        pd.DataFrame: A new DataFrame containing only the columns corresponding to the
                      specified CpGs in `cg_set`.
    """
    match1 = dat.columns.isin(cg_set)
    if not match1.any():
        missing_cpgs = len(cg_set) - match1.sum()
        print(f"{missing_cpgs} CpGs in the requested subset are missing from your data.")

    dat_reduced = dat.loc[:, match1]
    return dat_reduced
