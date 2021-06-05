import random

import click


MIN_n_m = 1
MAX_n_m = 1000

MIN_a_i = -1000000
MAX_a_i = 1000000-1  # -1 to easily convert a Toeplitz to non-Toeplitz


def generate_sample(n, m, toeplitz):
    matrix = []
    for _ in range(n):
        matrix.append([0 for _ in range(m)])

    for d in range(-n+1, m):
        r = min(d, 0)
        c = max(0, d)

        value = random.randint(MIN_a_i, MAX_a_i)
        while r < n and c < m:
            matrix[r][c] = value
            r += 1
            c += 1

    if not toeplitz and n-2 > 0 and m-2 > 0:
        r = random.randint(0, n-2)
        c = random.randint(0, m-2)
        matrix[r][c] = matrix[r+1][c+1] + 1

    print(n,m)
    for i in range(n):
        print(" ".join(map(str, matrix[i])))


@click.command()
@click.option("--n-rows", "-r", type=int,
              help="Number of rows.")
@click.option("--n-cols", "-c", type=int,
              help="Number of columns.")
@click.option("--toeplitz", "-t", type=int,
              help="Is Toeplitz? 1 if yes, 0 if not")
@click.option("--seed", "-s", type=int,
              help="Integer random seed.")
def main(n_rows, n_cols, toeplitz, seed):
    if seed is not None:
        random.seed(seed)

    n = random.randint(MIN_n_m, MAX_n_m) if n_rows is None else n_rows
    m = random.randint(MIN_n_m, MAX_n_m) if n_cols is None else n_cols
    toeplitz = random.randint(0, 1) if toeplitz is None else toeplitz
    generate_sample(n, m, toeplitz)


if __name__ == "__main__":
    main()
