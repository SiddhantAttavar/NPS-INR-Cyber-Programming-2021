# Take input
n = int(input())

# Create an array dp where dp[i] is answer for N = i + 1
dp = [1, 2]
for i in range(2, n):
	dp.append(dp[i - 1] + dp[i - 2])

# The answer is dp[n - 1]
print(dp[n - 1])
