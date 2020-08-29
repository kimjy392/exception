N = int(input())
dp = [10**6+1] * (N+1)
dp[1] = 0
for j in range(2, N+1):
    if j // 3 and not j % 3:
        dp[j] = min(dp[j], dp[j // 3] + 1)
    if j // 2 and not j % 2:
        dp[j] = min(dp[j], dp[j // 2] + 1)
    dp[j] = min(dp[j], dp[j-1]+1)
print(dp[N])