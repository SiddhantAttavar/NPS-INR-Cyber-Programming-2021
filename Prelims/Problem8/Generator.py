# Import random functions
from random import randint

def generate(subtask):
    # Print N
    if subtask == 1:
        n = randint(1, 100)
    elif subtask == 2:
        n = randint(1, 1000)
    else:
        n = randint(1, int(1e5))
    print(n)
    
    # Generate the array
    for _ in range(n):
        print(randint(int(-1e9), int(1e9)), end = ' ')

if __name__ == '__main__':
    generate(int(input('Enter the subtask: ')))
