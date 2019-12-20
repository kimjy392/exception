import sys
I = sys.stdin.readline
sys.setrecursionlimit(10**6)

def back(x, y, dir):
    global result
    if x == N-1 and y == N-1:
        result += 1
        return
    for i in range(3):
        if dirvisit[dir][i]:
            flag = 0
            for j in range(len(direction[dir][i])):
                if direction[dir][i]:
                    dx, dy = direction[dir][i][j]
                    tx = x + dx
                    ty = y + dy
                    if 0 > tx or tx >= N or 0 > ty or ty >= N:
                        flag = 1
                        break
                    elif -1 < tx < N and -1 < ty < N and board[tx][ty]:
                        flag = 1
                        break
            if not flag:
                back(x+direction[dir][i][-1][0], y+direction[dir][i][-1][1], i)

N = int(I())
board = [list(map(int, I().split())) for _ in range(N)]
direction = {0:[[(0, 1)],[], [(0, 1), (1, 0), (1, 1)]], 1:[[],[(1, 0)],[(0, 1), (1, 0), (1, 1)]], 2:[[(0, 1)],[(1, 0)], [(0, 1), (1, 0), (1, 1)]]}
result = 0
dirvisit = [[True, False, True], [False, True, True], [True, True, True]]
back(0, 1, 0) # x, y, dir
print(result)
#
import sys
I = sys.stdin.readline
sys.setrecursionlimit(10**6)

result = 0
def back(dt, x, y):
    global result
    if x == N - 1 and y == N-1:
        result += 1
    else:
        if dt == 1:
            if y + 1 < N and not board[x][y+1]:
                back(1, x, y+1)
            if x + 1 < N and y + 1 < N and board[x+1][y+1] == 0 and board[x][y+1] == 0 and board[x+1][y] == 0:
                back(3, x+1, y+1)
        elif dt == 2:
            if x + 1 < N and board[x+1][y] == 0:
                back(2, x+1, y)
            if x + 1 < N and y + 1 < N and board[x+1][y+1] == 0 and board[x][y+1] == 0 and board[x+1][y] == 0:
                back(3, x+1, y+1)
        else:
            if y + 1 < N and board[x][y+1] == 0:
                back(1, x, y + 1)
            if x + 1 < N and board[x+1][y] == 0:
                back(2, x+1, y)
            if x + 1 < N and y + 1 < N and board[x+1][y+1] == 0 and board[x][y+1] == 0 and board[x+1][y] == 0:
                back(3, x+1, y+1)

N = int(I())
board =[]
for _ in range(N):
    board.append(list(map(int, I().split())))
back(1, 0, 1)
print(result)