# Import random functions
from random import randint, shuffle, choice

def generate(subtask):
    # Print T
    t = randint(1, 1000)
    print(t)
    for _ in range(t):
        # Print N and K
        k = randint(100, 999)
        n = randint(5, int(1e9))
        print(k, n)

if __name__ == '__main__':
    generate(int(input('Enter the subtask: ')))
