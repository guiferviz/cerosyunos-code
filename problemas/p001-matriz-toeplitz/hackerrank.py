"""Move and rename tests from test format for oj Python package to Hackerrank.

Hackerrank expects tests in a zip following an structure like:
- output
  - output00.txt
  - output01.txt
  - ...
- input
  - input00.txt
  - input01.txt
  - ...
"""

import pathlib
import shutil
import os


INPUT_PATH = "tests"
OUTPUT_PATH = "tests_hackerrank"


def main():
    # Prepare output dirs.
    shutil.rmtree(OUTPUT_PATH)
    os.makedirs(OUTPUT_PATH, exist_ok=True)
    os.makedirs(f"{OUTPUT_PATH}/input", exist_ok=True)
    os.makedirs(f"{OUTPUT_PATH}/output", exist_ok=True)

    test_dir = pathlib.Path(INPUT_PATH)
    for i, f in enumerate(sorted(test_dir.rglob("*.in"))):
        name = f.name[:-3]  # remove ".in"
        shutil.copy(f"tests/{name}.in", f"{OUTPUT_PATH}/input/input{i:02d}.txt")
        shutil.copy(f"tests/{name}.out", f"{OUTPUT_PATH}/output/output{i:02d}.txt")
        print(name, "->", i)


if __name__ == "__main__":
    main()
