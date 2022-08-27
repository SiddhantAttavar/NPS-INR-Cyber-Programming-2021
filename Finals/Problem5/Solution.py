# Import cache
from functools import lru_cache

@lru_cache(maxsize = None)
def solve(x, i):
	if x == 0:
		return 1
	
	if x < 0:
		return 0
	
	if i < 0:
		return 0

	return solve(x, i - 1) + solve(x - a[i], i)

# Take input
n, m = map(int, input().split())
a = list(map(int, input().split()))

# Print the answer
print(solve(n, m - 1))
