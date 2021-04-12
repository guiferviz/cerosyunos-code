def solve(n, numbers):
    # TU PRECIOSO CÓDIGO AQUÍ.
    pass


def read_input():
    n = int(input())
    numbers = list(map(int, input().split()))

    return n, numbers


def main():
    t = int(input())
    for _ in range(t):
        n, numbers = read_input()
        missing_number = solve(n, numbers)
        print(missing_number)


if __name__ == "__main__":
    main()
