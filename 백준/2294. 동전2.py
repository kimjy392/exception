# def find(x):
#     if dp[x] != 100001:
#         return dp[x]
#
#     for coin in coins:
#         if x - coin >= 0:
#             if dp[coin] != 100001 and dp[x-coin] != 100001:
#                 dp[x] = min(dp[x], dp[coin] + dp[x-coin])
#             else:
#                 dp[x] = min(dp[x], find(coin) + find(x-coin))
#     return dp[x]
n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
# dp = [100001] * 100001
# dp[0] = 0
# for coin in coins:
#     dp[coin] = 1
# find(k)
# print(dp[k] if dp[k] != 100001 else -1)
dp = [100001] * (k+1)
dp[0] = 0
for coin in coins:
    for i in range(coin, k+1):
        dp[i] = min(dp[i], dp[i-coin]+1)
    print(dp)
print(dp[k] if dp[k] != 100001 else -1)