def solve(n, m, matrix):
    for i in range(n-1):
        for j in range(m-1):
            if matrix[i][j] != matrix[i+1][j+1]:
                return 0
    return 1


def read_input():
    n, m = list(map(int, input().split()))
    matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

    return n, m, matrix


def main():
    n, m, matrix = read_input()
    is_toeplitz = solve(n, m, matrix)
    print(is_toeplitz)


if __name__ == "__main__":
    main()
