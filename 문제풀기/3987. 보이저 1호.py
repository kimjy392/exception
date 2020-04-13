from collections import deque

def move(x, y, d):
    visit = [[[False for _ in range(4)] for _ in range(M)] for _ in range(N)]
    visit[x][y][d] = True
    stack = deque([(x, y, d)])
    cnt = 1
    while stack:
        x, y, d = stack.popleft()
        tx, ty = x + dx[d], y + dy[d]
        if -1 < tx < N and -1 < ty < M and not visit[tx][ty][d]:
            if board[tx][ty] == '/' or board[tx][ty] == '\\':
                d = direction[board[tx][ty]][d]
            if board[tx][ty] == 'C':
                break
            cnt += 1
            visit[tx][ty][d] = True
            stack.append((tx, ty, d))
        elif -1 < tx < N and -1 < ty < M and visit[tx][ty][d]:
            return -1
        else:
            break

    return cnt

N, M = map(int, input().split())

board = []
blackhall = []
for i in range(N):
    tmp = list(input())
    board.append(tmp)
    for j in range(M):
        if tmp[j] == 'C':
            blackhall.append((i, j))

PR, PC = map(int, input().split())
PR, PC = PR-1, PC-1
# 동 0 서 1 남 2 북 3
direction = {'/' : [3, 2, 1, 0], '\\': [2, 3, 0, 1]}
ene = ['R', 'L', 'D', 'U']
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
result = [0, 0]
for i in [3, 0, 2, 1]:
    tmp = move(PR, PC, i)
    if tmp == -1:
        result = [ene[i], 'Voyager']
        break
    else:
        if tmp > result[1]:
            result = [ene[i], tmp]
print(result[0])
print(result[1])
