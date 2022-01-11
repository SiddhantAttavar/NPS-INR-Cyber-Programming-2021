# Import random functions
from random import randint, shuffle, choice

def generate(subtask):
    # Print N and M
    n = randint(1, 250)
    m = randint(1, 50)
    print(n, m)
    
    # Print A
    a = [randint(1, 50) for _ in range(m)]
    print(*a)

if __name__ == '__main__':
    generate(int(input('Enter the subtask: ')))
