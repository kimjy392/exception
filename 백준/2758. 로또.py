dp = [[0] * 2001 for _ in range(11)]
for i in range(1, 2001):
    dp[0][i] = 1
for i in range(10):
    for j in range(1, 2000//2+1):
        for k in range(j*2, 2001):
            dp[i+1][k] += dp[i][j]

for _ in range(int(input())):
    n, m = map(int, input().split())
    print(sum(dp[n-1][:m+1]))
