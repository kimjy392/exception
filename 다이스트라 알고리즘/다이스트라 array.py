import heapq

V, E = map(int, input().split())
K = int(input())
G = [ [] for _ in range(V+1)]
q = []
for _ in range(E):
    u, v, w = map(int ,input().split())
    G[u].append((v, w))
visit = [0] * (V+1)
D = [1e9] * (V+1)

D[K] = 0
# for _ in range(V):
#     u, MIN = 0, 1e9
#     for i in range(1, V+1):
#         if not visit[i] and D[i] < MIN:
#             u, MIN = i, D[i]
#
#     visit[u] = 1
#
#     for e, w in G[u]:
#         if not visit[e] and D[u] + w < D[e]:
#             D[e] = D[u] + w
heapq.heappush(q, [0, K])
while q:
    d, u = heapq.heappop(q)
    if d > D[u]: continue
    visit[u] = 1
    for e, w in G[u]:
        if not visit[e] and D[u] + w < D[e]:
            D[e] = D[u] + w
            heapq.heappush(q, [D[e], e])

for i in range(1, V+1):
    if D[i] == 1e9:
        print('INF')
    else:
        print(D[i])