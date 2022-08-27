# Take input
n = int(input())

# Do a binary search to find the result
low = 0
high = n
res = 0
while low <= high:
    mid = (low + high) // 2
    if mid * (mid + 1) // 2 <= n:
        res = mid
        low = mid + 1
    else:
        high = mid - 1

# Print the result
print(res)
