
def solve_counting_sort(N, numbers):
    """Resuelve el problema usando algo similar a un counting sort.

    Tiempo: N.
    Espacio: N.
    """

    counts = [0,] * N
    for i in numbers:
        counts[i - 1] = 1

    for i, j in enumerate(counts):
        if j == 0:
            return i + 1


def solve_comparison_sort(N, numbers):
    """Resuelve el problema ordenando con un algoritmo basado en comparaciones.

    Tiempo: N log(N) debido a al Timsort, el algoritmo usado por Python en
        la función `sorted`. En resumen, cualquier algoritmo de ordenación
        basado en comparaciones tendrá esa complejidad.
    Espacio: N en el peor de los casos debido a que la ordenación no es
        in-place.
    """

    numbers = sorted(numbers)

    for i, j in zip(range(1, N+1), numbers):
        if i != j:
            return i


def solve_efficiently(N, numbers):
    """Resuelve el problema usando sumas de progresiones aritméticas.

    Tiempo: N.
    Espacio: 1.
    """

    expected_sum = ((1 + N) * N) // 2
    actual_sum = sum(numbers)

    missing_number = expected_sum - actual_sum
    return missing_number


def read_input():
    N = int(input())
    numbers = list(map(int, input().split()))

    return N, numbers


def main():
    t = int(input())
    for _ in range(t):
        N, numbers = read_input()
        #missing_number = solve_counting_sort(N, numbers)
        #missing_number = solve_comparison_sort(N, numbers)
        missing_number = solve_efficiently(N, numbers)
        print(missing_number)


if __name__ == "__main__":
    main()
