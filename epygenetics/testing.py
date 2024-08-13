import argparse

import pandas as pd
import pytest
import tabulate as tb

from epygenetics.test.data.clock_results import *
from epygenetics.test.data.text_consts import *


def print_comparison_output(title: str, methylCIPHER_data: pd.DataFrame, epygenetics_data: pd.DataFrame) -> None:
    print(title)
    print(methylCIPHER)
    print(tb.tabulate(methylCIPHER_data, headers='keys', tablefmt='pretty'))
    print()
    print(epygenetics)
    print(tb.tabulate(epygenetics_data, headers='keys', tablefmt='pretty'))
    print()


def methylCIPHER_comparison() -> None:
    print()

    print(output_delimiter)
    print(intro_output)
    print(output_delimiter)
    print()

    print("Following comparisons are run with a dna methylation data found in 'epygenetics/data/examples/exampleBetas.csv\n")
    print(output_delimiter)
    print_comparison_output("Biological Age and Mortality Predictors", methylCIPHER_type_1, epygenetics_type_1)

    print("Following comparisons are run with a dna methylation data found in 'epygenetics/data/examples/exampleBetas_2.csv")
    print("Pheno data can be found in 'epygenetics/data/examples/examplePheno_2.csv\n")
    print_comparison_output("PRC Pheno Age", methylCIPHER_prcPhenoAge_data, epygenetics_prcPhenoAge_data)
    print_comparison_output("NON PRC Pheno Age", methylCIPHER_nonPrcPhenoAge_data, epygenetics_nonPrcPhenoAge_data)

    print(output_delimiter)
    print_comparison_output("Cancer and Mitotic Rates Predictors", methylCIPHER_type_2, epygenetics_type_2)

    print(output_delimiter)
    print_comparison_output("Chronological Age Predictors", methylCIPHER_type_3, epygenetics_type_3)

    print(output_delimiter)
    print_comparison_output("Gestational And Pediatric Age Predictors", methylCIPHER_type_4, epygenetics_type_4)

    print(output_delimiter)
    print_comparison_output("Non Blood Predictors", methylCIPHER_type_5, epygenetics_type_5)

    print(output_delimiter)
    print_comparison_output("Trait Predictors", methylCIPHER_type_6, epygenetics_type_6)


def init_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run code automated testing.")
    parser.add_argument('-u', '--unit', action='store_true', help="Run unit tests only")
    parser.add_argument('-c', '--comparison', action='store_true', help="Run comparison with methylCIPHER package only")

    return parser


def testing() -> None:
    pd.set_option('display.max_rows', None)

    parser = init_parser()
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
