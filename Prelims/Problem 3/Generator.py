# Import random functions
from random import randint

def generate(subtask):
    # Print N
    n = randint(1, int(1e5))
    print(n)

    # Print the arrays A and B
    for i in range(n):
        print(randint(1, int(1e9)), end = ' ')
    print()
    for i in range(n):
        print(randint(1, int(1e9)), end = ' ')