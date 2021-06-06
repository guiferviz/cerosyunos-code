def es_toeplitz(n_filas, n_columnas, matriz):
    for i in range(n_columnas):
        if not es_diagonal_constante(0, i, matriz, n_filas, n_columnas):
            return False
    for i in range(1, n_filas):
        if not es_diagonal_constante(i, 0, matriz, n_filas, n_columnas):
            return False
    return True


def es_diagonal_constante(f, c, matriz, n_filas, n_columnas):
    primer_numero = matriz[f][c]
    f += 1
    c += 1
    while f < n_filas and c < n_columnas:
        if matriz[f][c] != primer_numero:
            return False
        f += 1
        c += 1
    return True


def read_input():
    n, m = list(map(int, input().split()))
    matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

    return n, m, matrix


def main():
    n, m, matrix = read_input()
    is_toeplitz = es_toeplitz(n, m, matrix)
    print(int(is_toeplitz))


if __name__ == "__main__":
    main()
