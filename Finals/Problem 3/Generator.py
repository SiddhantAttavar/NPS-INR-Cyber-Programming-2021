# Import random functions
from random import randint, shuffle, choice

def generateConnectedGraph(maxN, weighted = True):
    # Generate N and M
    n = randint(1, maxN)
    m = randint(n - 1, min(n * (n - 1) // 2, maxN))

    # Generate Spanning Tree
    p = [-1] * n
    s = [0]
    l = list(range(1, n))
    shuffle(l)
    for i in l:
        p[i] = choice(s)
        s.append(i)
    edges = [[p[i] + 1, i + 1, 1] for i in range(1, n)]
    
    # Generate remaining m - (n - 1) edges
    for _ in range(m - n + 1):
        u = randint(1, n)
        v = randint(1, n)
        while u == v:
            v = randint(1, n)
        edges.append([u, v, 1])
    
    # Add weights if required
    if weighted:
        for i in range(len(edges)):
            edges[i][2] = randint(1, int(1e9))

    # Print test case
    print(n, m)
    for u, v, w in edges:
        print(u, v, w)

def generateRandomTree(maxN):
    # Generate N and M
    n = randint(1, maxN)
    m = n - 1
    
    # Generate Tree
    p = [-1] * n
    s = [0]
    l = list(range(1, n))
    shuffle(l)
    for i in l:
        p[i] = choice(s)
        s.append(i)
    
    # Print testcase
    print(n, m)
    for i in range(1, n):
        print(p[i] + 1, i + 1, randint(1, int(1e9)))

def generate(subtask):
    if subtask == 1:
        generateConnectedGraph(int(1e5), weighted = False)
    elif subtask == 2:
        generateRandomTree(int(1e5))
    elif subtask == 3:
        generateConnectedGraph(100)
    elif subtask == 4:
        generateConnectedGraph(1000)
    else:
        generateConnectedGraph(int(1e5))

if __name__ == '__main__':
    generate(int(input('Enter the subtask: ')))
