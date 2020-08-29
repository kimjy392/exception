N, K = map(int ,input().split())

coins = [int(input()) for _ in range(N)]
idx = N-1
result = 0
while idx >= 0 and K > 0:
    if K - coins[idx] < 0:
        idx -= 1
    else:
        K -= coins[idx]
        result += 1
print(result)
