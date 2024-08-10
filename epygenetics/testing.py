import argparse
import pandas as pd
import tabulate as tb
import pytest

import data.test.clock_results

delimiter = "=========================================================================================================="


def methylCIPHER_comparison() -> None:
    print()

    print(delimiter)
    print("A comparsion of implemented clocks with package written in programming language R called methylCIPHER is shown.")
    print("Some of the epygenetics clocks had to use imputation and between all implemented imputations here is shown the one that yielded the best results.")
    print("Lin, Vidal-Bralo, Lee-Control, Lee-Robust, Lee-Refined-Robust, Mayne, PEDBE, Horvath2 all use KNN imputation.")
    print("Bohlin, Knight and DNAm Cortical use regulat imputation using pre-calculated median values of the golden standard sesame-450k-median.")
    print(delimiter)
    print()

    print("Following comparisons are run with a dna methylation data found in 'epygenetics/data/examples/exampleBetas.csv:")
    print()

    print(delimiter)
    print("Biological Age and Mortality Predictors")
    print("methylCIPHER")
    df = data.test.clock_results.methylCIPHER_type_1
    print(tb.tabulate(df, headers='keys', tablefmt='pretty'))
    print()
    print("epygenetics")
    df = data.test.clock_results.epygenetics_type_1
    print(tb.tabulate(df, headers='keys', tablefmt='pretty'))
    print()
    print("Following comparisons are run with a dna methylation data found in 'epygenetics/data/examples/exampleBetas_2.csv:")
    print("Pheno data can be found in 'epygenetics/data/examples/examplePheno_2.csv:")
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
    print()

    print(delimiter)
    print("Cancer and Mitotic Rates Predictors")
    print("methylCIPHER")
    df = data.test.clock_results.methylCIPHER_type_2
    print(tb.tabulate(df, headers='keys', tablefmt='pretty'))
    print()
    print("epygenetics")
    df = data.test.clock_results.epygenetics_type_2
    print(tb.tabulate(df, headers='keys', tablefmt='pretty'))
    print()

    print(delimiter)
    print("Chronological Age Predictors")
    print("methylCIPHER")
    df = data.test.clock_results.methylCIPHER_type_3
    print(tb.tabulate(df, headers='keys', tablefmt='pretty'))
    print()
    print("epygenetics")
    df = data.test.clock_results.epygenetics_type_3
    print(tb.tabulate(df, headers='keys', tablefmt='pretty'))
    print()

    print(delimiter)
    print("Gestational And Pediatric Age Predictors")
    print("methylCIPHER")
    df = data.test.clock_results.methylCIPHER_type_4
    print(tb.tabulate(df, headers='keys', tablefmt='pretty'))
    print()
    print("epygenetics")
    df = data.test.clock_results.epygenetics_type_4
    print(tb.tabulate(df, headers='keys', tablefmt='pretty'))
    print()

    print(delimiter)
    print("Non Blood Predictors")
    print("methylCIPHER")
    df = data.test.clock_results.methylCIPHER_type_5
    print(tb.tabulate(df, headers='keys', tablefmt='pretty'))
    print()
    print("epygenetics")
    df = data.test.clock_results.epygenetics_type_5
    print(tb.tabulate(df, headers='keys', tablefmt='pretty'))
    print()

    print(delimiter)
    print("Trait Predictors")
    print("methylCIPHER")
    df = data.test.clock_results.methylCIPHER_type_6
    print(tb.tabulate(df, headers='keys', tablefmt='pretty'))
    print()
    print("epygenetics")
    df = data.test.clock_results.epygenetics_type_6
    print(tb.tabulate(df, headers='keys', tablefmt='pretty'))
    print()


def testing() -> None:
    pd.set_option('display.max_rows', None)

    parser = argparse.ArgumentParser(description="Run code automated testing.")
    parser.add_argument('--unit', action='store_true', help="Run mypy")
    parser.add_argument('--comparison', action='store_true', help="Run flake8")

    args = parser.parse_args()

    if not any(vars(args).values()):
        methylCIPHER_comparison()
        pytest.main(["--no-header", "-v", "epygenetics/test"])
    else:
        if args.unit:
            pytest.main(["--no-header", "-v", "epygenetics/test"])
        if args.comparison:
            methylCIPHER_comparison()


if __name__ == "__main__":
    testing()
