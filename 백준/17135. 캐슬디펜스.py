from collections import deque
import copy

def bfs(x, y):
    visit = [[False] * M for i in range(N+1)]
    visit[x][y] = True
    stack = [(x, y, 0)]
    enemy = []
    flag = 0
    while stack:
        x, y, d = stack.pop(0)
        if d > D:
            break
        if board[x][y] == 1 and flag > 0 and flag == d:
            enemy.append((d, y, x))
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            tx = x + dx
            ty = y + dy
            if -1 < tx < N+1 and -1 < ty < M and not visit[tx][ty]:
                if board[tx][ty] == 1 and not flag:
                    flag = d + 1
                visit[tx][ty] = True
                stack.append((tx, ty, d+1))
    return enemy

def back(k, n):
    global result, board
    if len(select) == 3:
        res = 0
        tmp = copy.deepcopy(board)
        for _ in range(N):
            etmp = []
            for i in range(3):
                enemy = sorted(bfs(N, select[i]))
                if not enemy:
                    continue
                etmp.append((enemy[0][2], enemy[0][1]))
            for x, y in etmp:
                if board[x][y] == 1:
                    board[x][y] = 0
                    res += 1
            ar = board.pop()
            board.pop()
            board.appendleft([0] * M)
            board.append(ar)

        board = copy.deepcopy(tmp)
        if res > result:
            result = res
        return

    for i in range(k, n):
        select.append(i)
        board[-1][i] = 2
        back(i+1, n)
        select.pop()
        board[-1][i] = 0

N, M, D = map(int, input().split())

board = deque([list(map(int, input().split())) for _ in range(N)])
board.append([0]*M)
select = []
result = 0

back(0, M)
print(result)