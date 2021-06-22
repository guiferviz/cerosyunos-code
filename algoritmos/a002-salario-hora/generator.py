import random

import click


MIN_a_i = 1000
MAX_a_i = 10000000


def generate_sample():
    return random.randint(MIN_a_i, MAX_a_i-1)


@click.command()
@click.option("--test-cases", "-t", type=int,
              help="Number of test cases to generate in the same test file.")
@click.option("--seed", "-s", type=int,
              help="Integer random seed.")
def main(test_cases, seed):
    if seed is not None:
        random.seed(seed)

    t = random.randint(1, 50) if test_cases is None else test_cases

    print(t)
    for _ in range(t):
        n = generate_sample()
        print(n)


if __name__ == "__main__":
    main()
