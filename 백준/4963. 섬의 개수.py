import sys
sys.setrecursionlimit(1500)

def dfs(x, y):
    visit[x][y] = 1
    for dx, dy in direction:
        tx, ty = x + dx, y + dy
        if -1 < tx < h and -1 < ty < w and not visit[tx][ty] and board[tx][ty]:
            dfs(tx, ty)
direction = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
while 1:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    board = []
    for _ in range(h):
        tmp = list(map(int, input().split()))
        board.append(tmp)

    visit = [[0] * w for _ in range(h)]
    result = 0
    for i in range(h):
        for j in range(w):
            if not visit[i][j] and board[i][j]:
                dfs(i, j)
                result += 1

    print(result)