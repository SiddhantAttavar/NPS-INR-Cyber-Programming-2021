def solve():
    # Take input
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    # Initialize res and pair sum set
    res = 0
    freq = {}
    for i in range(2, n - 1):
        # Add pair sums to the set for j < i - 1
        for j in range(i - 1):
            freq[a[j] + a[i - 1]] = freq.get(a[j] + a[i - 1], 0) + 1
        
        # Add to final answer
        for j in range(i + 1, n):
            if k - (a[i] + a[j]) in freq:
                res += freq[k - (a[i] + a[j])]
    
    # Print result
    print(res)
        

if __name__ == '__main__':
    solve()