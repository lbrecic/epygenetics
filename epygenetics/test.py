import tabulate as tb
import pandas as pd

import data.test.clock_results


def methylCIPHER_comparison() -> None:
    print()

    print("First a comparsion of implemented clocks with package written in programming language R called methylCIPHER is shown.")
    print("Some of the epygenetics clocks had to use imputation and between all implemented imputations here is shown the one that yielded the best results.")
    print("Lin, Vidal-Bralo, Lee-Control, Lee-Robust, Lee-Refined-Robust, Mayne, PEDBE, Horvath2 all use KNN imputation.")
    print("Bohlin, Knight and DNAm Cortical use regulat imputation using pre-calculated median values of the golden standard sesame-450k-median.")
    print()
    print("After showing you the results of clocks implemented both in methylCIPHER and epygenetics, a (non)prc PhenoAge clocks results are shown for both.")
    print()

    print("methylCIPHER")
    df = data.test.clock_results.methylCIPHER
    print(tb.tabulate(df, headers='keys', tablefmt='pretty'))

    print()

    print("epygenetics")
    df = data.test.clock_results.epygenetics
    print(tb.tabulate(df, headers='keys', tablefmt='pretty'))

    print()

    print("methylCIPHER - PRC Pheno Age")
    df = data.test.clock_results.methylCIPHER_prcPhenoAge_data
    print(tb.tabulate(df, headers='keys', tablefmt='pretty'))

    print()

    print("epygenetics - PRC Pheno Age")
    df = data.test.clock_results.epygenetics_prcPhenoAge_data
    print(tb.tabulate(df, headers='keys', tablefmt='pretty'))

    print()

    print("methylCIPHER - NON PRC Pheno Age")
    df = data.test.clock_results.methylCIPHER_nonPrcPhenoAge_data
    print(tb.tabulate(df, headers='keys', tablefmt='pretty'))

    print()

    print("epygenetics - NON PRC Pheno Age")
    df = data.test.clock_results.epygenetics_nonPrcPhenoAge_data
    print(tb.tabulate(df, headers='keys', tablefmt='pretty'))

    print("================================================================================")
    print()


def test() -> None:
    pd.set_option('display.max_rows', None)

    methylCIPHER_comparison()


if __name__ == "__main__":
    test()
