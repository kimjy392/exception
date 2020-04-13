from collections import deque

def bfs(x, y, d):
    global result
    stack = deque([(x, y, d, 0, 0)])
    visit[x][y] = [(x, y, d, 0)]

    while stack:
        x, y, d, m, cnt = stack.popleft()
        tx, ty, td, tm = x, y, d, m
        flag = 0
        if board[x][y] in '><^v':
            td = direction[board[x][y]]
        elif board[x][y] == '_':
            if m == 0:
                td = 1
            else:
                td = 2
        elif board[x][y] == '|':
            if m == 0:
                td = 4
            else:
                td = 3
        elif board[x][y] == '?':
            flag = 1
            for i in range(1, 5):
                nx, ny = x + dx[i], y + dy[i]
                if nx >= R:
                    nx = 0
                elif nx < 0:
                    nx = R - 1
                if ny >= C:
                    ny = 0
                elif ny < 0:
                    ny = C - 1
                if (nx, ny, i, tm) not in visit[nx][ny]:
                    visit[tx][ty].append((nx, ny, i, tm))
                    stack.append((nx, ny, i, tm, cnt+1))

        elif board[x][y] == '@':
            result = 1
            print('#{} YES'.format(tc))
            break
        elif board[x][y].isdigit():
            tm = int(board[x][y])
        elif board[x][y] == '+':
            if m == 15:
                tm = 0
            else:
                tm += 1
        elif board[x][y] == '-':
            if m == 0:
                tm = 15
            else:
                tm -= 1

        if not flag:
            tx += dx[td]
            ty += dy[td]
            if tx >= R:
                tx = 0
            elif tx < 0:
                tx = R - 1
            if ty >= C:
                ty = 0
            elif ty < 0:
                ty = C - 1
            if (tx, ty, td, tm) not in visit[tx][ty]:
                visit[tx][ty].append((tx, ty, td, tm))
                stack.append((tx, ty, td, tm, cnt+1))

T = int(input())
for tc in range(1, T+1):
    R, C = map(int, input().split())
    board = [list(input()) for _ in range(R)]
    direction = {'<': 2, '>': 1, '^': 3, 'v': 4} # > - 1, < - 2, ^ - 3, v - 4
    dx = [0, 0, 0, -1, 1]
    dy = [0, 1, -1, 0, 0]
    d = 1
    memory = 0
    result = 0
    isin = 0
    for i in range(R):
        for j in range(C):
            if board[i][j] == '@':
                isin = 1
    visit = [[[(0, 0, 0, 0)] for _ in range(C)] for _ in range(R)]
    if isin:
        bfs(0, 0, d)
    if not result:
        print('#{} NO'.format(tc))