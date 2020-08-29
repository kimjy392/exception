N, M, K = map(int, input().split())

while K > 0:
    n = N // 2
    m = M
    if n < m:
        M -= m - n
        K -= m - n
    elif n > m:
        N -= (n - M) * 2
        K -= (n - M) * 2
    else:
        N, M = N-2, M-1
        K -= 3
print(min(N // 2, M))