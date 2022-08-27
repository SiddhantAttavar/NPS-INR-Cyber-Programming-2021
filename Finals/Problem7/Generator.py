# Import random functions
from random import randint, shuffle, choice

def generate(subtask):
    # Print T
    t = randint(1, 100)
    print(t, end = ' ')
    s = ''
    for i in range(ord('a'), ord('z') + 1):
        s += chr(i)
    m = list(s)
    shuffle(m)
    print(*m, sep = '')
    m += [i.upper() for i in m]
    m += ['_', '.', ',', '!', '?']
    for _ in range(t):
        s = ''
        l = randint(1, 100)
        for i in range(l):
            s += choice(m)
        print(s)

if __name__ == '__main__':
    generate(int(input('Enter the subtask: ')))
