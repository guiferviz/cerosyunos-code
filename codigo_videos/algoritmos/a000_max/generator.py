import random
import sys


MAX_a_i = 2147483648


def generate_sample(n):
    print(n)

    a = list()
    for i in range(n):
        a.append(random.randint(0, MAX_a_i-1))
    print(" ".join(map(str, a)))


def main():
    if len(sys.argv) == 3:
        n = int(sys.argv[1])
        random.seed(int(sys.argv[2]))
        t = 1
    else:
        t = random.randint(1, 50)
        n = random.randint(1, 100)

    print(t)
    for _ in range(t):
        generate_sample(n)


if __name__ == "__main__":
    main()
