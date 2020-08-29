def fivo(n):
    if n == 0 or n == 1:
        return n
    if memo[n]:
        return memo[n]
    else:
        memo[n] = fivo(n-1) + fivo(n-2)
        return memo[n]

N = int(input())
memo = [0] * (N+1)
memo[1] = 1
print(fivo(N))