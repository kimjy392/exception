

def back(h, k, n):
    global result
    if k == n:
        visit = [[False] * M for _ in range(N)]
        for x, y in blocks:
            visit[x][y] = True
        for x, y in block:
            visit[x][y] = True
        for vir in virus:
            stack = [vir]
            visit[vir[0]][vir[1]] = True

            while stack:
                x, y = stack.pop(0)
                for i in range(4):
                    tx = x + dx[i]
                    ty = y + dy[i]
                    if -1 < tx < N and -1 < ty < M and not visit[tx][ty] and board[tx][ty] == 0:
                        visit[tx][ty] = True
                        stack.append((tx, ty))
        tmp = 0
        for i in range(N):
            for j in range(M):
                if not visit[i][j]:
                    tmp += 1
        result = max(result, tmp)
        return

    for i in range(h, len(empty)):
        block.append(empty[i])
        back(i+1, k+1 , n)
        block.pop()


N, M = map(int, input().split())
result = 0
board = [list(map(int ,input().split())) for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
blocks = []
virus = []
empty = []
block = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            empty.append((i, j))
        elif board[i][j] == 2:
            virus.append((i, j))
        elif board[i][j] == 1:
            blocks.append((i, j))
back(0, 0, 3)
print(result)