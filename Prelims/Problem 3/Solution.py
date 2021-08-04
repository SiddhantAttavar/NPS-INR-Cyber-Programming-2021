# Take input
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Find the values of array c
c = [0] * n
for i in range(n):
    c[i] = a[i] * b[i]

# Print the result
print(*c)