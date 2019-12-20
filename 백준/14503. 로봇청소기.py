N, M = map(int, input().split())
x, y, d = map(int ,input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visit = [[False] * M for _ in range(N)]
direction = [3, 0, 1, 2]
di = {0: (0, -1), 1: (-1, 0), 2: (0, 1), 3: (1, 0)}
back = [(1, 0), (0, -1), (-1, 0), (0, 1)]
cnt = 0
result = 0
flag = 0
while True:
    if board[x][y] == 0 and not visit[x][y]: # 청소하기
        visit[x][y] = True
        result += 1
        continue
    if cnt == 4:
        dx, dy = back[d]
        tx = x + dx
        ty = y + dy
        if -1 < tx < N and -1 < ty < M and board[tx][ty] == 0:
            x = tx
            y = ty
            cnt = 0
            flag = 1
            continue
        else:
            break
    dx, dy = di[d]
    tx = x + dx
    ty = y + dy
    if -1 < tx < N and -1 < ty < M and board[tx][ty] == 0 and not visit[tx][ty]:
        x = tx
        y = ty
        d = direction[d]
        cnt = 0
    else:
        d = direction[d]
        cnt += 1
for d in visit:
    print(d)
print(result)
