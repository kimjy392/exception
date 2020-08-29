T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    G = [[] for _ in range(N+1)]
    for _ in range(M):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)
    visit = [0] * (N+1)
    key = [1e9] * (N+1)
    cnt = N
    key[1] = 0
    pi = [0] * (N+1)
    while cnt:
        u = MIN = 1e9
        for i in range(1, N+1):
            if not visit[i] and MIN > key[i]:
                u, MIN = i, key[i]
        visit[u] = 1

        for v in G[u]:
            if not visit[v] and key[v] > 1:
                key[v] = 1
                pi[v] = u
        cnt -= 1

    result = 0
    for i in range(1, N+1):
        if pi[i]:
            result += 1
    print(result)