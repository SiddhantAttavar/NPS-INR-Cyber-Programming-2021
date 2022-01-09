# Import random functions
from random import randint

def generate(subtask):
    # Print N and X
    if subtask == 1:
        n = randint(1, 1000)
    else:
        n = randint(1, int(1e5))
    a = [randint(1, int(1e9)) for _ in range(n)]
    a.sort()
    u = randint(1, n)
    v = randint(1, n)
    while u == v:
        v = randint(1, n)
    print(n, a[u] + a[v])
    print(*a)

if __name__ == '__main__':
    generate(int(input('Enter the subtask: ')))
