# Import random functions
from random import randint, choice

def generate(subtask):
    # Print N
    n = randint(1, int(1e5))
    print(n)

    # Print the details for N moves
    directions = ['U', 'D', 'L', 'R']
    for i in range(n):
        print(choice(directions), randint(1, 100))