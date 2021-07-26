# Import random functions
from random import randint

def generate(subtask):
    # Print N
    print(randint(1, 1000))

if __name__ == '__main__':
    generate(int(input('Enter the subtask: ')))