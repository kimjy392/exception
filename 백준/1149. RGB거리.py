N = int(input())
dp = [[1e9] * N for _ in range(N)]
colors = [list(map(int, input().split())) for _ in range(N)]
dp[0][0], dp[0][1], dp[0][2] = colors[0][0], colors[0][1], colors[0][2]
for i in range(1, N):
    color = colors[i]
    dp[i][0] = min(dp[i-1][1] + color[0], dp[i-1][2] + color[0])
    dp[i][1] = min(dp[i-1][0] + color[1], dp[i-1][2] + color[1])
    dp[i][2] = min(dp[i-1][0] + color[2], dp[i-1][1] + color[2])
print(min(dp[-1]))