import heapq

V, E = map(int, input().split())
G = [[] for _ in range(V+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    G[a].append((b, c))
    G[b].append((a, c))
q = []

visit = [0] * (V+1)
cnt = V
key = [2147483648] * (V+1)
key[1] = 0
heapq.heappush(q, (0, 1))
while q:
    d, u = heapq.heappop(q)
    if d > key[u]:
        continue
    visit[u] = 1

    for v, w in G[u]:
        if not visit[v] and key[v] > w:
            key[v] = w
            heapq.heappush(q, (w, v))
print(sum(key[1:]))