
# epygenetics

`epygenetics` is a Python library designed to facilitate the execution, analysis, and testing of various epigenetic clocks. The library is built following the latest PEP8 standards and provides a comprehensive toolset for researchers and data scientists working in the field of epigenetics.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [Execution](#execution)
  - [Testing](#testing)
- [Implemented Epigenetic Clocks](#implemented-epigenetic-clocks)
- [Contributing](#contributing)
- [License](#license)

## Installation

To install the `epygenetics` library, clone the repository and install the necessary dependencies:

```bash
git clone https://github.com/lbrecic/epygenetics.git
cd epygenetics
pip install -r requirements.txt
```

## Usage

The `epygenetics` library provides three main entry points: execution, analysis, and testing. Each entry point can be executed via the command line using the following format:

```bash
python -m epygenetics.<method_name> --flags...
```

### Execution

To run an epigenetic clock, use the `execution` method. The following example demonstrates how to execute a specific clock:

```bash
python -m epygenetics.execution -c <clock_name> -d <dnam_file> [options]
```

#### Example:

```bash
python -m epygenetics.execution -c Horvath1 -d path/to/dnam_file.csv -p path/to/pheno_file.csv -i -f path/to/imputation_file.csv -m regular -v
```

**Flags:**

- `-c, --clock`: **(Required)** Name of the clock to execute.
- `-d, --dnam`: **(Required)** Path to DNA methylation betas file.
- `-p, --pheno`: Path to the pheno file (optional).
- `-i, --imputation`: Impute missing CpG values (optional).
- `-f, --imputation-file`: Path to CpG imputation file (optional).
- `-m, --imputation-method`: Imputation method to use (optional, default: \`regular\`).
- `-v, --verbose`: Show traceback if an error occurs (optional).

### Testing

To run the automated tests provided in the library, use the `testing` method. The following example demonstrates how to execute the tests:

```bash
python -m epygenetics.testing [options]
```

#### Example:

```bash
python -m epygenetics.testing -u
```

**Flags:**

- `-u, --unit`: Run unit tests only.
- `-c, --comparison`: Run comparison with the methylCIPHER package only.

## Implemented Epigenetic Clocks

The following epigenetic clocks have been implemented in the `epygenetics` library:

- HRS in CH PhenoAge (HRSInChPhenoAge)
- Non PRC PhenoAge (non_prcPhenoAge)
- PRC PhenoAge (prcPhenoAge)
- PhenoAge (PhenoAge)
- EpiTOC (EpiTOC)
- HypoClock (hypoClock)
- MiAge (MiAge)
- Bocklandt (Bocklandt)
- Garagnani (Garagnani)
- Hannum (Hannum)
- Horvath Multi-Tissue (Horvath1)
- Lin (Lin)
- Vidal-Bralo (VidalBralo)
- Weidner (Weidner)
- Zhang (Zhang)
- Bohlin (Bohlin)
- Knight (Knight)
- Lee Control (LeeControl)
- Lee Robust (LeeRobust)
- Lee Refined-Robust (LeeRefinedRobust)
- Mayne (Mayne)
- PEDBE (PEDBE)
- DNA Methylation Cortical Clock (DNAmClockCortical)
- Horvath Skin & Blood (Horvath2)
- Alcohol McCartney (Alcohol_McCartney)
- BMI McCartney (BMI_McCartney)
- Smoking McCartney (Smoking_McCartney)

## Contributing

Contributions to the `epygenetics` library are welcome. Please submit pull requests or open issues on the [GitHub repository](https://github.com/lbrecic/epygenetics).

Before contributing, please ensure that your code adheres to the PEP8 standards and passes all tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
