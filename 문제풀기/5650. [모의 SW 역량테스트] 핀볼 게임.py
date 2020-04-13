def move(x, y, d):
    res = 0
    start = (x, y)
    while 1:
        tx, ty = x + dx[d], y + dy[d]
        if -1 < tx < N and -1 < ty < N:
            if board[tx][ty] == -1 or (tx, ty) == start:
                return res
            elif 0 < board[tx][ty] < 6:
                blocknum = board[tx][ty]
                d = block[blocknum][d]
                res += 1
            elif board[tx][ty] >= 6:
                hallnum = board[tx][ty]
                if hall1[hallnum] == (tx, ty):
                    x, y = hall2[hallnum]
                else:
                    x, y = hall1[hallnum]
                continue
            x, y = tx, ty
        else:
            d = block[5][d]
            res += 1
            x, y = tx, ty

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    board = []
    hall1 = [0] * 11
    hall2 = [0] * 11
    for i in range(N):
        tmp = list(map(int, input().split()))
        board.append(tmp)
        for j in range(len(tmp)):
            if tmp[j] >= 6:
                if not hall1[tmp[j]]:
                    hall1[tmp[j]] = (i, j)
                elif not hall2[tmp[j]]:
                    hall2[tmp[j]] = (i ,j)

    # 동 0 서 1 남 2 북 3
    block = {1 : [1, 3, 0, 2], 2 : [1, 2, 3, 0], 3 : [2, 0, 3, 1], 4 : [3, 0, 1, 2], 5:[1, 0, 3, 2]}
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    result = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                for k in range(4):
                    tmp = move(i, j, k)
                    if tmp > result:
                        result = tmp
    print('#{} {}'.format(tc, result))
