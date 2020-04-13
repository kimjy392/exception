N, M, K = map(int, input().split())
notebook = dict()

for _ in range(K):
    R, C = map(int, input().split())
    sticker = [list(map(int, input().split())) for _ in range(R)]
    flg = 0
    for _ in range(4):
        curx, cury = 0, 0
        while curx < N and cury < M:
            tmp = dict()
            flag = 0
            for j in range(R):
                for k in range(C):
                    if sticker[j][k] == 1 and curx+j < N and cury+k < M and not notebook.get((curx+j, cury+k)):
                        tmp[(curx+j,cury+k)] = 1
                    elif sticker[j][k] == 0:
                        continue
                    else:
                        flag = 1
                        break
                if flag:
                    break
            if not flag:
                notebook.update(tmp)
                flg = 1
                break
            cury += 1
            if cury == M:
                cury = 0
                curx += 1
        if not flg:
            sticker_tmp = [[0] * R for _ in range(C)]
            for j in range(R):
                for k in range(C):
                    if sticker[j][k] == 1:
                        sticker_tmp[k][R - 1 - j] = 1
            R, C = C, R
            sticker = sticker_tmp
        else:
            break

print(len(notebook))
board = [[0] * M for _ in range(N)]
for key in notebook:
    x, y = key
    board[x][y] = 1
for d in board:
    print(d)