T = int(input())

for tc in range(1, T+1):
    N = int(input())
    board = []
    MAX = 0
    for _ in range(N):
        tmp = list(map(int, input().split()))
        board.append(tmp)
        for i in range(N):
            if MAX < tmp[i]:
                MAX = tmp[i]
    result = -1
    for i in range(N-2):
        for j in range(1, N-1):
            x, y = i, j
            for d1 in range(1, N):
                lx, ly = x + (d1*1), y + (d1*-1)
                if -1 < lx < N and -1 < ly < N:
                    for d2 in range(1, N):
                        rx, ry = x+d2, y+d2
                        ex, ey = lx + d2, ly + d2
                        if -1 < rx < N and -1 < ry < N and -1 < ex < N and -1 < ey < N:
                            res = 0
                            pdesert = [0] * (MAX + 1)
                            flag = 0
                            for k in range(d1+1):
                                tx, ty = x + (k*1), y+(k * -1)
                                nx, ny = rx + (k*1), ry+(k * -1)
                                if pdesert[board[tx][ty]]:
                                    flag = 1
                                    break
                                pdesert[board[tx][ty]] = 1
                                if pdesert[board[nx][ny]]:
                                    flag = 1
                                    break
                                pdesert[board[nx][ny]] = 1
                            for k in range(1, d2):
                                tx, ty = x + k, y + k
                                nx, ny = lx + k, ly + k
                                if pdesert[board[tx][ty]]:
                                    flag = 1
                                    break
                                pdesert[board[tx][ty]] = 1
                                if pdesert[board[nx][ny]]:
                                    flag = 1
                                    break
                                pdesert[board[nx][ny]] = 1
                            if flag:
                                continue
                            res = sum(pdesert)
                            if res > result:
                                result = res
                        else:
                            break
                else:
                    break
    print('#{} {}'.format(tc, result))
