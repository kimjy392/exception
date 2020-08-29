# N = int(input())
#
# wines = [int(input()) for _ in range(N)] + [0]
# dp = [0] * (N+1)
# dp[0] = wines[0]
# dp[1] = wines[0] + wines[1]
# for i in range(2, N):
#     dp[i] = max(dp[i-1], dp[i-2]+wines[i], dp[i-3]+wines[i-1]+wines[i])
# print(max(dp))

def solve():
    d[1], d[2] = p[1], p[1]+p[2]
    for i in range(3, n+1):
        d[i] = d[i-1]
        d[i] = max(d[i], d[i-2]+p[i])
        d[i] = max(d[i], d[i-3]+p[i-1]+p[i])

n = int(input())
d = [0]*(n+2)
p = [0]+[int(input()) for _ in range(n)]+[0]
solve()
print(d[n])
