
def solve_counting_sort(n, numbers):
    """Resuelve el problema usando algo similar a un counting sort.

    Tiempo: n.
    Espacio: n.
    """

    counts = [0,] * n
    for i in numbers:
        counts[i - 1] = 1

    for i, j in enumerate(counts):
        if j == 0:
            return i + 1


def solve_comparison_sort(n, numbers):
    """Resuelve el problema ordenando con un algoritmo basado en comparaciones.

    Tiempo: n log(n) debido a al Timsort, el algoritmo usado por Python en
        la función `sorted`. En resumen, cualquier algoritmo de ordenación
        basado en comparaciones tendrá esa complejidad.
    Espacio: n en el peor de los casos debido a que la ordenación no es
        in-place.
    """

    numbers = sorted(numbers)

    for i, j in enumerate(numbers):
        if i + 1 != j:
            return i + 1
    return n


def solve_arithmetic_progression(n, numbers):
    """Resuelve el problema usando sumas de progresiones aritméticas.

    Tiempo: n.
    Espacio: 1.
    """

    expected_sum = ((1 + n) * n) // 2
    actual_sum = sum(numbers)

    missing_number = expected_sum - actual_sum
    return missing_number


def solve_inplace_sort(n, numbers):
    """Bonus track :)

    Tiempo: n.
    Espacio: 1.
    """

    numbers.append(-1)
    i = 0
    while i < n:
        c = numbers[i]
        while c > 0 and numbers[c - 1] > 0:
            c_prev = c
            c = numbers[c - 1]
            numbers[c_prev - 1] = 0
        i += 1

    for i, j in enumerate(numbers):
        if j != 0:
            return i + 1


def read_input():
    n = int(input())
    numbers = list(map(int, input().split()))

    return n, numbers


def main():
    t = int(input())
    for _ in range(t):
        n, numbers = read_input()
        #missing_number = solve_comparison_sort(n, numbers)
        #missing_number = solve_counting_sort(n, numbers)
        missing_number = solve_arithmetic_progression(n, numbers)
        #missing_number = solve_inplace_sort(n, numbers)
        print(missing_number)


if __name__ == "__main__":
    main()
