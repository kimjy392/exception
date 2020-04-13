from collections import deque

R, C = map(int, input().split())

board = []
mouse = []
water = deque()
result = 0
flag = 0
xy = []
visit = [[0] * C for _ in range(R)]
for i in range(R):
    tmp = list(input())
    board.append(tmp)
    for j in range(len(tmp)):
        if tmp[j] == 'S':
            mouse = deque([(i, j, 0)])
        elif tmp[j] == '*':
            water.append((i, j, 0))
            flag = 1
        elif tmp[j] == 'D':
            xy = [i, j]

if flag:
    visit[xy[0]][xy[1]] = 9999
    while water:
        x, y, d = water.popleft()
        for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
            tx, ty = x + dx, y + dy
            if -1 < tx < R and -1 < ty < C and not visit[tx][ty] and (board[tx][ty] == '.' or board[tx][ty] == 'S'):
                visit[tx][ty] = d+1
                water.append((tx, ty, d+1))
visit2 = [[0] * C for _ in range(R)]
visit2[mouse[0][0]][mouse[0][1]] = 1
while mouse:
    x, y, d = mouse.popleft()
    if board[x][y] == 'D':
        result = d
        break
    for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
        tx, ty = x + dx, y + dy
        if flag and -1 < tx < R and -1 < ty < C and (visit[tx][ty] > d+1 or visit[tx][ty] == 0)and not visit2[tx][ty] and (board[tx][ty] == '.' or board[tx][ty] == 'D'):
            mouse.append((tx, ty, d+1))
            visit2[tx][ty] = 1
        if not flag and -1 < tx < R and -1 < ty < C and not visit2[tx][ty] and  (board[tx][ty] == '.' or board[tx][ty] == 'D'):
            mouse.append((tx, ty, d+1))
            visit2[tx][ty] = 1

if not result:
    print('KAKTUS')
else:
    print(result)