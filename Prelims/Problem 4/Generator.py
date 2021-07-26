# Import random functions
from random import randint

def generate(subtask):
    # Print N
    n = randint(1, int(1e5))
    print(n)

    # Print the data of each student
    for _ in range(n):
        # Generate random name
        nameLength = randint(1, 100)
        name = ''
        for i in range(nameLength):
            name += chr(randint(ord('A'), ord('Z')))

        # Print name with random marks and age
        print(name, randint(1, int(1e9), randint(1, int(1e9))))