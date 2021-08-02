# Import random functions
from random import randint, sample

def generate(subtask):
    # Generate N and K
    if subtask == 1:
        n = randint(1, 50)
    elif subtask == 2:
        n = randint(1, 100)
    else:
        n = randint(1, 1000)
    k = randint(int(8e8), int(1e9))
    print(n, k)

    # Generate the array A
    a = [randint(1, k) for _ in range(n)]
    
    # Change a few at random to increase the answer
    numToChange = randint(1, n // 4)
    indexes = list(range(n))
    for _ in range(numToChange):
        p, q, r, s = sorted(sample(indexes, 4))
        if a[p] + a[q] + a[r] > k:
            # Reduce all by a third
            a[p] //= 3
            a[q] //= 3
            a[r] //= 3
        # Change the last num to make the sum k
        a[s] = k - (a[p] + a[q] + a[r])

    # Print the array
    print(*a)

if __name__ == '__main__':
    generate(int(input('Enter the subtask: ')))