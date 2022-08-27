# Import random functions
from random import randint, shuffle, choice

def generate(subtask):
    # Print N
    if subtask == 1:
        n = randint(1, 9)
    else:
        n = randint(1, int(1e5))
    print(n)
    
    # Print A
    a = [randint(1, 1000) for _ in range(n)]
    print(*a)

if __name__ == '__main__':
    generate(int(input('Enter the subtask: ')))
