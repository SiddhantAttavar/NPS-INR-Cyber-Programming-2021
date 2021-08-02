def solve():
    # Take input
    n = int(input())
    square = [list(map(int, input())) for _ in range(n)]

    # Find the number of ones in each row and column
    rowOnes = [0] * n
    colOnes = [0] * n
    for i in range(n):
        for j in range(n):
            if square[i][j]:
                rowOnes[i] += 1
                colOnes[j] += 1
    
    # For each row and column if the number of ones is x
    # The number of pairs we can form is x * (x - 1) / 2
    res = 0
    for ones in rowOnes + colOnes:
        res += ones * (ones - 1) // 2
    
    # Print result
    print(res)

if __name__ == '__main__':
    solve()