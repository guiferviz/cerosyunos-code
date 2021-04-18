def solve_python_buildin(n, numbers):
    return min(numbers)


def solve_custom_implementation(n, numbers):
    assert numbers

    min_so_far = numbers[0]
    for i in numbers[1:]:
        if i < min_so_far:
            min_so_far = i

    return min_so_far


def read_input():
    n = int(input())
    numbers = list(map(int, input().split()))

    return n, numbers


def main():
    t = int(input())
    for _ in range(t):
        n, numbers = read_input()
        max_number = solve_custom_implementation(n, numbers)
        print(max_number)


if __name__ == "__main__":
    main()
