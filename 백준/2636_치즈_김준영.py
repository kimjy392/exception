def air(x, y):
    airstack = [(x, y)]

    while airstack:
        x, y = airstack.pop(0)
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if -1 < tx < N and -1 < ty < M and board[tx][ty] == 0 and not airvisit[tx][ty]:
                airvisit[tx][ty] = True
                airstack.append((tx, ty))
def melt(x, y):
    visit[x][y] = True
    stack = [(x, y)]
    count = 0

    while stack:
        x, y = stack.pop(0)
        flag = 0
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if -1 < tx < N and -1 < ty < M and board[tx][ty] == 1 and not visit[tx][ty]:
                stack.append((tx, ty))
                visit[tx][ty] = True
            elif -1 < tx < N and -1 < ty < M and airvisit[tx][ty] and board[tx][ty] == 0:
                flag = 1
                board[x][y] = 0
        if flag:
            count += 1
    return count


N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

time = 0
result = 0
a = 0
while 1:
    visit = [[False] * M for _ in range(N)]
    airvisit = [[False] * M for _ in range(N)]
    air(0, 0)
    # 치즈 갯수 확인
    curcheeze = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                curcheeze += 1
    if curcheeze == 0:
        break
    time += 1
    # 녹이기
    tmp = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1 and not visit[i][j]:
                tmp += melt(i, j)
    result = tmp
print(time)
print(result)
