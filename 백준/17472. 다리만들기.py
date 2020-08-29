def grouping(x, y, group):
    visit[x][y] = group
    stack = [[x, y]]
    while stack:
        x, y = stack.pop(0)
        for i in range(4):
            tx, ty = x + dx[i], y + dy[i]
            if -1 < tx < N and -1 < ty < M and not visit[tx][ty] and board[tx][ty]:
                visit[tx][ty] = group
                stack.append([tx, ty])

def find_distance(x, y, group):
    for i in range(4):
        tx, ty = x + dx[i], y + dy[i]
        tmp = 0
        while -1 < tx < N and -1 < ty < M:
            if visit[tx][ty] == 0:
                tmp += 1
            elif visit[tx][ty] == group:
                break
            else:
                if distance.get((visit[tx][ty], group)):
                    if tmp >= 2:
                        distance[(visit[tx][ty], group)] = min(distance[(visit[tx][ty], group)], tmp)
                else:
                    if tmp >= 2:
                        distance[(visit[tx][ty], group)] = tmp
                        if not visit[tx][ty] in G[group]:
                            G[group].append(visit[tx][ty])
                            G[visit[tx][ty]].append(group)
                break
            tx, ty = tx + dx[i], ty + dy[i]
def dfs(u):
    if dvisit[u]:
        return
    dvisit[u] = True
    for v in G[u]:
        if not dvisit[v]:
            dfs(v)

N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
visit = [[0] * M for _ in range(N)]
cnt = 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
for i in range(N):
    for j in range(M):
        if not visit[i][j] and board[i][j]:
            cnt += 1
            grouping(i, j, cnt)

G = [[] for _ in range(cnt + 1)]
distance = dict()
for i in range(N):
    for j in range(M):
        if visit[i][j]:
            find_distance(i, j, visit[i][j])

mvisit = [0] * (cnt+1)
key = [1e9] * (cnt + 1)
V = cnt + 1
key[1] = 0
flag = 0
dvisit = [0] * (cnt + 1)
dfs(1)
if sum(dvisit) == cnt:
    flag = 1
if flag:
    while cnt:
        u = MIN = 1e9
        for i in range(1, V):
            if not mvisit[i] and key[i] < MIN:
                u, MIN = i, key[i]

        mvisit[u] = 1
        for v in G[u]:
            w = distance[(u, v)]
            if not mvisit[v] and key[v] > w:
                key[v] = w
        cnt -= 1

    print(sum(key[1:]))
else:
    print(-1)