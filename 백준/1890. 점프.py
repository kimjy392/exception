N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]
dp[0][0] = 1
for i in range(N):
    for j in range(N):
        if i == N-1 and j == N -1:
            break
        tx, ty = i + board[i][j], j + board[i][j]
        if -1 < tx < N:
            dp[tx][j] += dp[i][j]
        if -1 < ty < N:
            dp[i][ty] += dp[i][j]
print(dp[-1][-1])