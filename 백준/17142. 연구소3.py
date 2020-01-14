def bfs(lst):
    stack = selectv[:]
    visit = [[0] * N for _ in range(N)]
    res = 0
    cnt = len(stack)
    for x, y, d in stack:
        visit[x][y] = 1
    while stack:
        x, y, d = stack.pop(0)
        if board[x][y] == 0:
            cnt += 1
            res = d
        for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
            tx = x + dx
            ty = y + dy
            if -1 < tx < N and -1 < ty < N and not visit[tx][ty] and (board[tx][ty] == 0 or board[tx][ty] == 2):
                stack.append([tx, ty, d+1])
                visit[tx][ty] = visit[x][y] + 1
    if cnt == room:
        return res
    else:
        return -1
def back(k, n):
    global result
    if len(selectv) == M:
        time = bfs(selectv)
        if time != -1:
            if result > time:
                result = time
        return

    for i in range(k, n):
        selectv.append(virusus[i])
        back(i+1, n)
        selectv.pop()
N, M = map(int, input().split())

board = []
virusus = []
result = 0xfffff
room = 0
for i in range(N):
    tmp = list(map(int, input().split()))
    board.append(tmp)
    for j in range(N):
        if tmp[j] == 2:
            virusus.append([i, j, 0])
            room += 1
        if tmp[j] == 0:
            room += 1
room = room -(len(virusus) - M)
selectv = []
back(0, len(virusus))
if result == 0xfffff:
    print(-1)
else:
    print(result)