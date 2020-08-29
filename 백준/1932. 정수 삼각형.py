N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dp = []
for i in range(N-1):
    dp.append([0] * (i+1))
dp.append(board[N-1][:])
for i in range(N-2, -1, -1):
    for j in range(len(dp[i])):
        dp[i][j] = max(board[i][j] + dp[i+1][j], board[i][j] + dp[i+1][j+1])
print(dp[0][0])