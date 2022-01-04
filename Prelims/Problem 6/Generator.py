# Import random functions
from random import randint

def generate(subtask):
    # Print N
    if subtask == 1:
        print(randint(1, int(1e5)))
    else:
        print(randint(1, int(1e9)))

if __name__ == '__main__':
    generate(int(input('Enter the subtask: ')))
