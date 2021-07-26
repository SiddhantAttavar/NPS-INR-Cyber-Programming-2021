def solve():
    # Take input
    n = int(input())
    a = list(map(int, input().split()))

    # Create an array best which is the largest sum of a 
    # contiguous subarray that ends at the current index
    best = [0] * n
    best[0] = a[0]
    for i in range(1, n):
        best[i] = max(best[i-1] + a[i], a[i])

    # The answer is the maximum number in best
    print(max(best))

if __name__ == '__main__':
    solve()