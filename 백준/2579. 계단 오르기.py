N = int(input())
stairs = [int(input()) for _ in range(N)] + [0]
dp = [0] * (N+1)

dp[0], dp[1] = stairs[0], stairs[0] + stairs[1]
for i in range(2, N):
    dp[i] = max(dp[i-2]+stairs[i], dp[i-3]+stairs[i-1]+stairs[i])
print(dp[N-1])

