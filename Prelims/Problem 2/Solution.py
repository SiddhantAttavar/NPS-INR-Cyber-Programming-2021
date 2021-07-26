def solve():
    # Take input
    n = int(input())

    # Print the squares of the first n natural numbers
    for i in range(1, n+1):
        print(i * i, end = ' ')

if __name__ == '__main__':
    solve()