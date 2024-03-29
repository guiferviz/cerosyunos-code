
import random
import sys


def generate_sample(n):
    print(n)

    a = list(range(1, n+1))
    random.shuffle(a)
    del a[random.randint(0, n-1)]
    print(" ".join(map(str, a)))

def main():
    if len(sys.argv) == 3:
        n = int(sys.argv[1])
        random.seed(int(sys.argv[2]))
        t = 1
    else:
        t = random.randint(1, 100)
        n = random.randint(1, 50)

    print(t)
    for _ in range(t):
        generate_sample(n)


if __name__ == "__main__":
    main()
