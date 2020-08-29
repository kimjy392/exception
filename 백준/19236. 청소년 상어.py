from copy import deepcopy

board = [[[] for _ in range(4)]  for _ in range(4)]

fishxy = dict()
for i in range(4):
    fishes = list(map(int, input().split()))
    for j in range(0, len(fishes), 2):
        a, b = fishes[j], fishes[j+1]
        idx = j // 2
        board[i][idx].append(a)
        board[i][idx].append(b-1)
        fishxy[a] = (i, idx)
direction = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
res = board[0][0][0]
fishxy[board[0][0][0]] = ()
board[0][0] = [-1, board[0][0][1]]
stack = [(board, fishxy, [0, 0], res)]
result = 0
while stack:
    tboard, tfishxy, shark, res = stack.pop(0)
    if result < res:
        result = res

    for i in range(1, 17):
        if not tfishxy[i]:
            continue
        fx, fy = tfishxy[i]
        num, d = tboard[fx][fy]
        for j in range(8):
            dx, dy = direction[(j+d) % 8]
            tx, ty = fx + dx, fy + dy
            tboard[fx][fy][1] = (j+d) % 8
            if -1 < tx < 4 and -1 < ty < 4 and [tx, ty] != shark:
                if tboard[tx][ty][0] > 0:
                    tfishxy[tboard[fx][fy][0]], tfishxy[tboard[tx][ty][0]] = tfishxy[tboard[tx][ty][0]], tfishxy[tboard[fx][fy][0]]
                elif tboard[tx][ty][0] == 0:
                    tfishxy[num] = (tx, ty)
                tboard[fx][fy], tboard[tx][ty] = tboard[tx][ty], tboard[fx][fy]
                break
    cnt = 1
    while 1:
        sx, sy = shark
        sdx, sdy = direction[tboard[sx][sy][1]]
        nx, ny = sx + sdx * cnt, sy + sdy * cnt
        if -1 < nx < 4 and -1 < ny < 4 and tboard[nx][ny][0] > 0:
            tres = res + tboard[nx][ny][0]
            tmp_b = deepcopy(tboard)
            tmp_f = deepcopy(tfishxy)
            tmp_b[sx][sy] = [0, 0]
            tmp_f[tmp_b[nx][ny][0]] = ()
            tmp_b[nx][ny] = [-1, tmp_b[nx][ny][1]]
            stack.append((tmp_b, tmp_f, [nx, ny], tres))
        cnt += 1
        if cnt > 4:
            break

print(result)

