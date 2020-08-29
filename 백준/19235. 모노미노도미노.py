from collections import deque
def attach(kind, tiles, board):
    tmp = []
    for tile in tiles:
        idx = 0
        y = tile
        for i in range(6):
            if board[i][y]:
                break
            else:
                idx = i
        tmp.append(idx)
    mtmp = min(tmp)
    if kind == 1 or kind == 2:
        for tile in tiles:
            y = tile
            board[mtmp][y] = kind
    else:
        y = tiles[0]
        board[mtmp][y] = 1
        board[mtmp-1][y] = 1

def remove(board):
    global result
    flag = 1
    while flag:
        flag = 0
        tmp = []
        for i in range(6):
            cnt = 0
            for j in range(4):
                if board[i][j]:
                    cnt += 1
            if cnt == 4:
                board[i] = [0] * 4
                flag = 1
                result += 1
                tmp.append(i)
                break
        if flag:
            for s in tmp:
                for i in range(s, -1, -1):
                    for j in range(4):
                        if board[i][j] == 1:
                            board[i][j] = 0
                            idx = minx(i, j, board)
                            board[idx][j] = 1
                        elif board[i][j] == 2:
                            board[i][j], board[i][j + 1] = 0, 0
                            idxs = []
                            idxs.append(minx(i, j, board))
                            idxs.append(minx(i, j+1, board))
                            idx = min(idxs)
                            board[idx][j] = 2
                            board[idx][j+1] = 2


def minx(x, y, board):
    idx = x
    for k in range(x, 6):
        if board[k][y] == 0:
            idx = k
        elif board[k][y] == 1 or board[k][y] == 2:
            break
    return idx

# r의 x값이 b의 y = 3-x 값이 된다
def tile(kind, x, y):
    if kind == 1:
        return [(y, ), (3-x, )]
    elif kind == 2:
        return [(y, y+1), (3-x, 3-x)]
    else:
        return [(y, y), (3-x, 3-x-1)]
def isline(board):
    for i in range(2):
        if 1 in board[i] or 2 in board[i]:
            board.pop()
            board.appendleft([0]* 4)

N = int(input())

bluebor = deque([[0] * 4 for _ in range(6)])
greenbor = deque([[0] * 4 for _ in range(6)])
switch = {'G': [0, 1, 2, 3], 'B': [0, 1, 3, 2]}
result = 0
total = 0
for a in range(N):
    t, x, y = map(int, input().split())
    greentile, bluetile = tile(t, x, y)
    attach(switch['B'][t], bluetile, bluebor)
    attach(switch['G'][t], greentile, greenbor)

    remove(greenbor)
    remove(bluebor)

    isline(greenbor)
    isline(bluebor)

for i in range(6):
    for j in range(4):
        if greenbor[i][j]:
            total += 1
        if bluebor[i][j]:
            total += 1

print(result)
print(total)


