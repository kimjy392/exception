def bfs(x, y):
    global result
    stack = [(x, y, 0)]
    visit = [[False] * M for _ in range(N)]
    visit[x][y] = True
    while stack:
        x, y, dis = stack.pop(0)
        result = max(result, dis)
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if -1 < tx < N and -1 < ty < M and board[tx][ty] == 'L' and not visit[tx][ty]:
                visit[tx][ty] = True
                stack.append((tx, ty, dis+1))

N, M = map(int, input().split())

board = [list(input()) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
result = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 'L':
            bfs(i, j)

print(result)