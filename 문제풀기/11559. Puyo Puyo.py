from collections import deque

def move():
    for j in range(M):
        stack = []
        for i in range(N):
            if board[i][j] != '.':
                stack.append(board[i][j])
                board[i][j] = '.'
        idx = N - 1
        while stack:
            value = stack.pop()
            board[idx][j] = value
            idx -= 1


def bfs(nx, ny):
    stack = deque([(nx, ny)])
    cnt = [(nx, ny)]
    value = board[nx][ny]
    board[nx][ny] = '.'
    while stack:
        x, y = stack.popleft()
        for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
            tx, ty = x + dx, y + dy
            if -1 < tx < N and -1 < ty < M and value == board[tx][ty]:
                board[tx][ty] = '.'
                stack.append((tx, ty))
                cnt.append((tx, ty))
    if len(cnt) <= 3:
        for x, y in cnt:
            board[x][y] = value
        return 0
    if len(cnt) >= 4:
        return len(cnt)

N, M = 12, 6
board = [list(input()) for _ in range(N)]
result = 0
isremove = 1
while isremove:
    isremove = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] != '.':
                    isremove += bfs(i, j)
    move()
    result += 1

print(result - 1)