# Import random functions
from random import randint

def generate(subtask):
    # Print N
    if subtask == 1:
        n = randint(1, 5)
    elif subtask == 2:
        n = randint(1, 15)
    else:
        n = randint(1, int(1e5))
    print(n)

if __name__ == '__main__':
    generate(int(input('Enter the subtask: ')))
