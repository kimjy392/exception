def bfs(x, y, ra):
    stack = [(x, y)]
    visit[x][y] = True
    while stack:
        x, y = stack.pop(0)
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if -1 < tx < N and -1 < ty < N and ra < board[tx][ty] and not visit[tx][ty]:
                stack.append((tx, ty))
                visit[tx][ty] = True

N = int(input())
board = []
MAX = 0
result = 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
for i in range(N):
    tmp = list(map(int, input().split()))
    num = max(tmp)
    if num > MAX:
        MAX = num
    board.append(tmp)
for rain in range(0, MAX+1):
    visit = [[False] * N for _ in range(N)]
    tmp = 0
    for i in range(N):
        for j in range(N):
            if rain < board[i][j] and not visit[i][j]:
                bfs(i, j, rain)
                tmp += 1
    if result < tmp:
        result = tmp

print(result)