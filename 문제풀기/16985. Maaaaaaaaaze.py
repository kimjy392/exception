
def bfs(fx, fy, fz):
    global result
    visit = [[[0] * 5 for _ in range(5)] for _ in range(5)]
    visit[fx][fy][fz] = 1
    stack = [(fx, fy, fz)]

    while stack:
        x, y, z = stack.pop(0)
        if x == 4 and y == 4 and z == 4 and d[(order[x], direction[order[x]])][y][z]:
            return visit[x][y][z]
        if result < visit[x][y][z]:
            return
        for i in range(6):
            tx, ty, tz = x + dx[i], y + dy[i], z + dz[i]
            if -1 < tx < 5 and -1 < ty < 5 and -1 < tz < 5 and not visit[tx][ty][tz] and d[(order[tx], direction[order[tx]])][ty][tz]:
                visit[tx][ty][tz] = visit[x][y][z] + 1
                stack.append((tx, ty, tz))

    return 0xfffff

def rotate(lst):
    tmp = [[0] * 5 for _ in range(5)]
    for j in range(4, -1, -1):
        line = lst[4 - j]
        for k in range(5):
            tmp[k][j] = line[k]
    return tmp

def back2(k, n):
    if k == n:
        back(0, 5)
        return
    for i in range(5):
        if i not in order:
            order.append(i)
            back2(k+1, n)
            order.pop()



def back(k, n):
    global result
    if result == 12:
        return
    if k == n:
        if d[(order[0], direction[order[0]])][0][0]:
            res = bfs(0, 0, 0)
            if res == None:
                return
            if result > res:
                result = res
        return
    for i in range(4):
        direction.append(i)
        back(k + 1, n)
        direction.pop()


board = []
result = 0xfffff
for i in range(5):
    tmp = [list(map(int, input().split())) for _ in range(5)]
    board.append(tmp)

d = dict({(0, 0): board[0],
          (1, 0): board[1],
          (2, 0): board[2],
          (3, 0): board[3],
          (4, 0): board[4]}
         )
for i in range(5):
    for j in range(0, 3):
        d[(i, j + 1)] = rotate(d[(i, j)])
direction = []
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
order = []
back2(0, 5)
if result == 0xfffff:
    print(-1)
else:
    print(result-1)