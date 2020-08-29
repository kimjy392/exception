N = int(input())

numbers = list(map(int, input().split()))
dp = [0] * N
dp[0] = numbers[0]

for i in range(1, N):
    dp[i] = numbers[i]
    dp[i] = max(dp[i-1]+numbers[i], dp[i])
print(max(dp))