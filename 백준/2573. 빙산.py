def melt(x, y):
    count = 0
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if -1 < tx < N and -1 < ty < M and binvisit[tx][ty]:
            count += 1
    if board[x][y] - count >= 0:
        board[x][y] -= count
    else:
        board[x][y] = 0

def check(x, y):
    stack = [(x, y)]
    visit[x][y] = True
    while stack:
        x, y =  stack.pop(0)
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if -1 < tx < N and -1 < ty < M and not visit[tx][ty] and board[tx][ty]:
                stack.append((tx, ty))
                visit[tx][ty] = True

N, M = map(int ,input().split())

board = [list(map(int, input().split())) for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
time = 0
flag = 0
while time < 3:
    visit = [[False] * M for _ in range(N)]
    binvisit = [[False] * M for _ in range(N)]
    # 빙산이 분리되었는지 확인 or 빙산의 갯수가 0 이 되는지 확인
    tmp = 0
    bingsan = []
    for i in range(N):
        for j in range(M):
            if board[i][j] and not visit[i][j]:
                check(i, j)
                tmp += 1
            if board[i][j]:
                bingsan.append((i, j))
            else:
                binvisit[i][j] = True
    if tmp > 1:
        flag = 1
        break

    if len(bingsan) == 0:
        flag = 2
        break

    time += 1
    for i in range(len(bingsan)):
        melt(bingsan[i][0], bingsan[i][1])
if flag == 1:
    print(time)
else:
    print(0)
