N = int(input())
dp = [0] * (90+1)

dp[0], dp[1], dp[2] = 0, 1, 1
for i in range(3, N+1):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[N])