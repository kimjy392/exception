def back(k, n, x, y, res):
    if k == n:
        result.add(int(res))
        return

    for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
        tx, ty = x+dx, y+dy
        if -1 < tx < 4 and -1 < ty < 4:
            back(k+1, n, tx, ty, res+str(board[tx][ty]))




T = int(input())

for tc in range(1, T+1):
    board = [list(map(int, input().split())) for _ in range(4)]
    result = set()
    for i in range(4):
        for j in range(4):
            back(0, 6, i, j, str(board[i][j]))
    print('#{}'.format(tc), len(result))