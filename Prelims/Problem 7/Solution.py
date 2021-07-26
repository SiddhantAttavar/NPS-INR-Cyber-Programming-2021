def solve():
    # Take input
    n, q = map(int, input().split())
    grid = [[False] * n for i in range(n)]
    for i in range(n):
        row = input()
        for j in range(n):
            grid[i][j] = row[j] == '1'

    # Create a prefix sum table
    prefSum = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(n):
            prefSum[i + 1][j + 1] = prefSum[i][j + 1] + prefSum[i + 1][j] - prefSum[i][j] + grid[i][j]

    # For each query, print the answer
    for _ in range(q):
        x1, y1, x2, y2 = map(int, input().split())
        print(prefSum[x2][y2] - prefSum[x1 - 1][y2] - prefSum[x2][y1 - 1] + prefSum[x1 - 1][y1 - 1])

if __name__ == '__main__':
    solve()