def DFS(x, y, res, cnt):
    global result
    if result < res:
        result = res
    for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
        tx, ty = x + dx, y + dy
        if 0 > tx or N-1 < tx or 0 > ty or N-1 < ty:
            continue
        if not visit[tx][ty] and board[tx][ty] < board[x][y]:
            visit[tx][ty] = True
            DFS(tx, ty, res+1, cnt)
            visit[tx][ty] = False
        if cnt == 0 and board[tx][ty] - k >= 0 and board[x][y] <= board[tx][ty] and  board[x][y] > board[tx][ty] - k and not visit[tx][ty]:
            tmp = board[tx][ty]
            board[tx][ty] = board[tx][ty] - k
            visit[tx][ty] = True
            DFS(tx, ty, res+1, 1)
            visit[tx][ty] = False
            board[tx][ty] = tmp

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    MAX = 0
    start = []
    result = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == MAX:
                start.append((i, j))
            elif board[i][j] > MAX:
                start = [(i, j)]
                MAX = board[i][j]
    for i, j in start:
        for k in range(1, K+1):
            visit = [[False] * N for _ in range(N)]
            visit[i][j] = True
            DFS(i, j, 1, 0)
    print('#{} {}'.format(tc, result))