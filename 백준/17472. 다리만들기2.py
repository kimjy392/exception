def back(k, n):
    if k == n:
        print(bridge)
        return
    bridge.append(k)
    back(k+1, n)
    bridge.pop()
    back(k+1, n)

def bfs(x, y, number):
    stk = [(x, y)]
    stack = [(x, y)]
    visit[x][y] = True
    board[x][y] = number
    while stack:
        x, y = stack.pop(0)
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            tx = x + dx
            ty = y + dy
            if -1 < tx < N and -1 < ty < M and not visit[tx][ty] and board[tx][ty]:
                visit[tx][ty] = True
                stack.append((tx, ty))
                board[tx][ty] = number
                stk.append((tx, ty))
    return stk
N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
visit = [[False]*M for _ in range(N)]
cnt = 1
land = 0
lands = []
for i in range(N):
    for j in range(M):
        if board[i][j] and not visit[i][j]:
            lands.append(bfs(i, j, cnt))
            cnt += 1
        if board[i][j]:
            land += 1
bri = []

for k in range(len(lands)):
    for xy in lands[k]:
        x, y = xy
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            tx = x + dx
            ty = y + dy
            if -1 < tx < N and -1 < ty < M and not board[tx][ty]:
                tmp = []
                while -1 < tx < N and -1 < ty < M:
                    if board[tx][ty]:
                        tmp.sort()
                        if tmp not in bri:
                            bri.append(tmp)
                        break
                    tmp.append((tx, ty))
                    tx += dx
                    ty += dy
bridge = []
back(0, len(bri))


