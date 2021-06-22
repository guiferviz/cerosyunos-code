import random

import click


MIN_a_i = 0
MAX_a_i = 2147483648


def generate_sample(n):
    print(n)

    a = [random.randint(MIN_a_i, MAX_a_i-1) for _ in range(n)]
    print(" ".join(map(str, a)))


@click.command()
@click.option("--test-cases", "-t", type=int,
              help="Number of test cases to generate in the same test file.")
@click.option("--n-numbers", "-n", type=int,
              help="Number of input numbers per test case.")
@click.option("--seed", "-s", type=int,
              help="Integer random seed.")
def main(test_cases, n_numbers, seed):
    if seed is not None:
        random.seed(seed)

    t = random.randint(1, 50) if test_cases is None else test_cases
    n = random.randint(1, 100) if n_numbers is None else n_numbers

    print(t)
    for _ in range(t):
        generate_sample(n)


if __name__ == "__main__":
    main()
