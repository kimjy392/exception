def dfs(x, y, ex, ey, cnt, res):
    global result
    if cnt == 4:
        if result < res:
            result = res
        return
    nx, ny = [], []
    MAX = 0
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        tx = x + dx
        ty = y + dy
        if -1 < tx < N and -1 < ty < M and (tx, ty) != (ex, ey):
            if MAX < board[tx][ty]:
                MAX = board[tx][ty]
                nx = [tx]
                ny = [ty]
            elif MAX == board[tx][ty]:
                nx.append(tx)
                ny.append(ty)
    for i in range(len(nx)):
        dfs(nx[i], ny[i], x, y, cnt+1, res+MAX)

N, M = map(int,input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dt = [[(0, 1), (0, 2), (-1, 1)], [(0, 1), (0, 2), (1, 1)], [(1, 0), (2, 0), (1, 1)], [(1, 0), (2, 0), (1, -1)]]
result = 0
for i in range(N):
    for j in range(M):
        dfs(i, j, i, j, 0, 0)
        for k in range(4):
            res = board[i][j]
            for dx, dy in dt[k]:
                tx = i + dx
                ty = j + dy
                if -1 < tx < N and -1 < ty < M:
                   res += board[tx][ty]
                else:
                    res = 0
                    break
            if res > result:
                result = res
print(result)