# Import random functions
from random import randint

def generate(subtask):
    # Generate N and K
    if subtask == 1:
        n = randint(1, 100)
    elif subtask == 2:
        n = randint(1, 1000)
    print(n)

    # Generate the square
    for i in range(n):
        for j in range(n):
            print(randint(0, 1), end = '')
        print()

if __name__ == '__main__':
    generate(int(input('Enter the subtask: ')))