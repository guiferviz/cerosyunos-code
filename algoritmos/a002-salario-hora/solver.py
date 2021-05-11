def solve(salario_anual):
    salario_mensual = salario_anual / 12
    salario_dia = salario_mensual / 20
    salario_hora = salario_dia / 8
    return salario_hora


def main():
    t = int(input())
    for _ in range(t):
        salario_anual = int(input())
        salario_hora = solve(salario_anual)
        print(f"{salario_hora:.2f}")


if __name__ == "__main__":
    main()
