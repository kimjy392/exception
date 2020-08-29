N = int(input())
arr = list(map(int, input().split()))
dp = [0] * N
dp[0] = 1
for i in range(1, N):
    dp[i] = 1
    for j in range(i):
        if arr[i] > arr[j] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
print(max(dp))
