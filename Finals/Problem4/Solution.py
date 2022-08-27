# Take input
n = int(input())
a = list(map(int, input().split()))

# Sort a in descending order, and calculate the final result
a.sort(reverse = True)
res = 0
for i in range(n):
	res += (1 << i) * a[i]
print(res)
