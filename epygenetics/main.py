import argparse
import sys
import traceback
from typing import Optional
from warnings import simplefilter

import pandas as pd

from epygenetics.clocks.factory import ClockFactory
from epygenetics.clocks.type import ClockType
from epygenetics.imputers.type import ImputerType


def setup() -> None:
    simplefilter(action="ignore", category=pd.errors.PerformanceWarning)


def init_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Clock Execution Script")

    parser.add_argument('--clock', type=str, required=True, help="Name of the clock to execute")
    parser.add_argument('--dnam', type=str, required=True, help="Path to DNA methylation betas file")
    parser.add_argument('--pheno', type=str, required=False, help="Path to pheno file")
    parser.add_argument('--imputation', required=True, action='store_true', help="Impute missing CpG values")
    parser.add_argument('--imputation-file', type=str, required=False, help="Path to CpG imputation file")
    parser.add_argument('--imputation-method', type=str, required=False, default='regular', help="Imputation method to use")
    parser.add_argument('--verbose', action='store_true', help="Show traceback if an error occurs")

    return parser


def main() -> None:
    setup()

    parser = init_parser()
    args = parser.parse_args()

    try:
        # Set traceback verbosity
        if not args.verbose:
            sys.tracebacklimit = 0

        # Load DNA methylation betas
        dna_m: pd.DataFrame = pd.read_csv(args.dnam)

        # Load pheno data if provided
        pheno: Optional[pd.DataFrame] = pd.read_csv(args.pheno) if args.pheno else None

        is_imputation: bool = args.imputation

        # Load CpG imputation method if provided
        imputation_type = ImputerType.from_str(args.imputation_method)

        cpg_imputation: Optional[pd.DataFrame] = None
        if is_imputation:
            # Load CpG imputation data if provided
            cpg_imputation = pd.read_csv(args.imputation_file) if args.imputation_file else None

        # Create clock
        clock_type: ClockType = ClockType.from_str(args.clock)
        clock = ClockFactory.create_clock(clock_type)

        # Execute clock
        clock.execute(dna_m, pheno, is_imputation, imputation_type, cpg_imputation)

    except Exception as e:
        if args.verbose:
            traceback.print_exc()
        else:
            print(f"An error occurred: {e}")
            print('Please try choosing a clock from the following list:')
            ClockType.list_predefined_clocks()


if __name__ == "__main__":
    main()
