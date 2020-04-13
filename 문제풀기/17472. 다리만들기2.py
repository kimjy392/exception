def dfs(x, y, count):
    visit[x][y] = True
    board[x][y] = count
    for dx, dy in (-1, 0), (1, 0), (0, 1), (0, -1):
        tx, ty = x+dx, y+dy
        if -1 < tx < N and -1 < ty < M and not visit[tx][ty] and board[tx][ty]:

            dfs(tx, ty, count)

N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
visit = [[False]*M for _ in range(N)]
cnt = 1
for i in range(N):
    for j in range(M):
        if not visit[i][j] and board[i][j]:
            dfs(i, j, cnt)
            cnt += 1
bridges = dict()
for i in range(N):
    for j in range(M):
        if board[i][j]:
            for dx, dy in (-1, 0), (1, 0), (0, 1), (0, -1):
                tmp = []
                while 1:
                    tx, ty = i + dx, j + dy
                    if -1 < tx < N and -1 < ty < M and not board[tx][ty]:
                        tmp.append((tx, ty))
                    elif -1 < tx < N and -1 < ty < M and board[tx][ty] > 0 and board[tx][ty] != board[i][j]:
                        if bridges.get((board[tx][ty], board[i][j])) or bridges.get((board[i][j], board[tx][ty])):

                        break

