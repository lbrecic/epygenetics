import subprocess
import argparse


def run_command(command: str) -> None:
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running command: {command}")
        print(result.stdout)
        print(result.stderr)
    else:
        print(result.stdout)


def run_mypy() -> None:
    print("Running mypy...")
    run_command("mypy .")


def run_flake8() -> None:
    print("Running flake8...")
    run_command("flake8 .")


def run_isort() -> None:
    print("Running isort...")
    run_command("isort .")


def main() -> None:
    parser = argparse.ArgumentParser(description="Run code quality checks.")
    parser.add_argument('--mypy', action='store_true', help="Run mypy")
    parser.add_argument('--flake8', action='store_true', help="Run flake8")
    parser.add_argument('--isort', action='store_true', help="Run isort")

    args = parser.parse_args()

    if not any(vars(args).values()):
        run_mypy()
        run_flake8()
        run_isort()
    else:
        if args.mypy:
            run_mypy()
        if args.flake8:
            run_flake8()
        if args.isort:
            run_isort()


if __name__ == "__main__":
    main()
