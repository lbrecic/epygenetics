import subprocess


def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running command: {command}")
        print(result.stdout)
        print(result.stderr)
    else:
        print(result.stdout)


def run_mypy():
    print("Running mypy...")
    run_command("mypy .")


def run_flake8():
    print("Running flake8...")
    run_command("flake8 .")


def run_isort():
    print("Running isort...")
    run_command("isort .")


def main():
    run_mypy()
    run_flake8()
    run_isort()


if __name__ == "__main__":
    main()
