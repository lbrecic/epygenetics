import pandas as pd
from custom_regression_clock import CustomRegressionClock
from epygenetics.clocks.base_clocks.clock import Clock
from epygenetics.loader.loader import AbstractLoader
from epygenetics.loader.strategies.csv import CSVLoader


def main():
    loader: AbstractLoader = CSVLoader()
    cpgs: pd.DataFrame = loader.load_data('../data/examples/exampleCpGs.csv')
    clock: Clock = CustomRegressionClock(cpgs)
    dna_m: pd.DataFrame = loader.load_data('../data/examples/exampleBetas.csv')
    clock.execute(dna_m)

if __name__ == '__main__':
    main()


# from custom_clock import CustomClock
# clock = CustomClock()
    # dna_m = pd.read_csv('../data/examples/exampleBetas.csv')
    # clock.execute(dna_m)