# Import random functions
from random import randint

def generate(subtask):
    # Print N
    n = randint(1, 1000)

    # Generate the grid
    for i in range(n):
        for j in range(n):
            print(randint(0, 1), end = '')
        print()
    
    # Generate Q
    if subtask == 1:
        q = 1
    else:
        q = randint(1, int(1e5))
    
    for _ in range(q):
        # Print the subrectangle
        x1 = randint(1, n)
        x2 = randint(1, n)
        y1 = randint(1, n)
        y2 = randint(1, n)

        if x1 > x2:
            x1, x2 = x2, x1
        if y1 > y2:
            y1, y2 = y2, y1
        
        print(x1, x2, y1, y2)

if __name__ == '__main__':
    generate(int(input('Enter the subtask: ')))