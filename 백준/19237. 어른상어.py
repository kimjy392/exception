def scent():
    for idx, value in enumerate(sharks):
        if idx == 0 or value == 0:
            continue
        smell[value[0]][value[1]] = [idx, k]
def find(shark, curd):
    if sharks[shark] == 0:
        return
    x, y = sharks[shark]
    tmp = []
    for i in range(0, 4):
        dx, dy = direction[prior[shark][curd][i]]
        tx, ty = x + dx, y + dy
        if -1 < tx < N and -1 < ty < N and smell[tx][ty] == [0, 0]:
            board[x][y] = 0
            dshark[shark] = prior[shark][curd][i]
            if board[tx][ty]:
                if board[tx][ty] < shark:
                    sharks[shark] = 0
                else:
                    sharks[shark] = (tx, ty)
                    board[tx][ty] = shark
            else:
                board[tx][ty] = shark
                sharks[shark] = (tx, ty)
            return

        elif -1 < tx < N and -1 < ty < N and smell[tx][ty][0] == shark:
            tmp.append((tx, ty, prior[shark][curd][i]))
    if tmp:
        board[x][y] = 0
        board[tmp[0][0]][tmp[0][1]] = shark
        sharks[shark] = (tmp[0][0], tmp[0][1])
        dshark[shark] = tmp[0][2]
    return



N, M, k = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
dshark = [0] + list(map(int, input().split()))
sharks = [0] * (M+1)
for i in range(N):
    for j in range(N):
        if board[i][j]:
            sharks[board[i][j]] = (i, j)
direction = [[],[-1, 0], [1, 0], [0, -1], [0, 1]]
prior = [[] for _ in range(M+1)]
for i in range(M*4):
    if not i % 4:
        prior[(i//4)+1].append([])
    prior[(i//4)+1].append(list(map(int, input().split())))
smell = [[[0, 0] for _ in range(N)] for _ in range(N)]

for time in range(1, 1001):
    scent()
    for i in range(1, M+1):
        find(i, dshark[i])
    for i in range(N):
        for j in range(N):
            if smell[i][j] != [0, 0]:
                smell[i][j][1] -= 1
                if smell[i][j][1] == 0:
                    smell[i][j] = [0, 0]
    cnt = 0
    for shark in sharks:
        if shark == 0:
            continue
        cnt += 1
    if cnt == 1:
        print(time)
        break
else:
    print(-1)