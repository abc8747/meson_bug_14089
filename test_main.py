import subprocess
from pathlib import Path

PATH_BUILD = Path(__file__).parent / "build"


def assert_output_equals(executable_name: str, expected_output: str) -> None:
    for path in PATH_BUILD.glob(f"{executable_name}*"):
        if path.is_file():
            result = subprocess.check_output([str(path)], cwd=PATH_BUILD, shell=True)
            assert result.strip() == expected_output.encode()
            return
    else:
        raise FileNotFoundError(
            f"Executable {executable_name} not found in {PATH_BUILD}"
        )


def test_c():
    assert_output_equals("main_c", "C compilation is working.")


def test_f():
    assert_output_equals("main_f", "Fortran compilation is working.")
