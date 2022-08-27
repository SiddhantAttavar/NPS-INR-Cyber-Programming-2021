# Take input
n, x = map(int, input().split())
a = list(map(int, input().split()))

# Identify i and j
l = 0
r = n - 1
while l < r:
	if (a[l] + a[r]) == x:
		print(l + 1, r + 1)
		break
	if (a[l] + a[r]) < x:
		l += 1
	else:
		r -= 1
else:
	print(l + 1, r + 1)
