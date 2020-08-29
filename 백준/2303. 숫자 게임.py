N = int(input())

cards = [list(map(int, input().split())) for _ in range(N)]

dp = [0] * N
dp2 = [[[0 for _ in range(5)] for _ in range(3)] for _ in range(N)]

for i in range(N):
    card = cards[i]
    for j in range(3):
        for k in range(j+1, 5):
            dp2[i][j][k] = card[j] + card[k]
            for e in range(k+1, 5):
                dp[i] = max(dp[i], (dp2[i][j][k] + card[e]) % 10)
result = 0
tmp = 0
for i in range(N):
    if dp[i] >= tmp:
        result = i
        tmp = dp[i]
print(result+1)