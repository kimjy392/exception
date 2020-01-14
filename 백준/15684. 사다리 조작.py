N, M, H = map(int, input().split())
ladders = [[0] * (M*2+1) for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    ladders[a][2*b] = 1
for i in range(N+1):
    for j in range(1, M+1):
        ladders[i][j*2-1] = 1
for d in ladders:
    print(d)