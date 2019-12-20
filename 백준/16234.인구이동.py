def bfs(x, y):
    divpop = 0
    conxy = [(x, y)]
    conpop = board[x][y]
    stack = [(x, y)]
    visit[x][y] = True

    while stack:
        x, y = stack.pop(0)
        curpop = board[x][y]
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if -1 < tx < N and -1 < ty < N and not visit[tx][ty] and L <= abs(curpop - board[tx][ty]) <= R:
                stack.append((tx, ty))
                conxy.append((tx, ty))
                conpop += board[tx][ty]
                visit[tx][ty] = True
    if len(conxy) == 1:
        return
    else:
        divpop = conpop // len(conxy)
        for x, y in conxy:
            board[x][y] = divpop
        return
N, L, R = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
result = 0
flag = 1
while flag:
    visit = [[False] * N for _ in range(N)]
    flag = 0

    for i in range(N):
        for j in range(N):
            if not visit[i][j]:
                for k in range(4):
                    tx = i + dx[k]
                    ty = j + dy[k]
                    if -1 < tx < N and -1 < ty < N and L <= abs(board[tx][ty] - board[i][j]) <= R and not visit[tx][ty]:
                        bfs(i, j)
                        flag = 1
                        break
    if flag:
        result += 1

print(result)

