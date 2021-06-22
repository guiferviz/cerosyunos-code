def solve(salario_anual):
    # TU PRECIOSO CÓDIGO AQUÍ.
    pass


def main():
    t = int(input())
    for _ in range(t):
        salario_anual = int(input())
        salario_hora = solve(salario_anual)
        print(f"{salario_hora:.2f}")


if __name__ == "__main__":
    main()
