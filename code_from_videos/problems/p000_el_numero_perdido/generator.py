
import random
import sys


def generate_sample(n):
    print(n)

    a = list(range(n))
    random.shuffle(a)
    del a[random.randint(0, n-1)]
    print(" ".join(map(str, a)))

def main():
    if len(sys.argv):
        t = random.randint(1, 100)
        n = random.randint(1, 50)
    else:
        n = int(sys.argv[1])
        random.seed(int(sys.argv[2]))
        t = 1

    print(t)
    for _ in range(t):
        generate_sample(n)


if __name__ == "__main__":
    main()
