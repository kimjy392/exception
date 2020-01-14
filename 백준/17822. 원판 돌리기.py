from collections import deque
import sys
sys.setrecursionlimit(10000)
def dfs(x, y, n):
    global flag, isfind, M
    visit[x][y] = True

    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if 0 < tx < N+1 and -1 < ty < M and not visit[tx][ty] and board[tx][ty] == n:
            board[tx][ty] = 0
            isfind = True
            flag = 1
            dfs(tx, ty, n)
    if y == 0 and N+1 > x > 0:
        if board[x][M-1] == num:
            board[x][M-1] = 0
            isfind = True
            flag = 1
            dfs(x, M-1, n)
    if y == M - 1 and N+1 > x > 0:
        if board[x][0] == num:
            board[x][0] = 0
            isfind = True
            flag = 1
            dfs(x, 0, n)


def rotate(x, di, k):
    for _ in range(k):
        if not di:
            for i in range(x, N+1, x):
                end = board[i].pop()
                board[i].appendleft(end)
        else:
            for i in range(x, N+1, x):
                start = board[i].popleft()
                board[i].append(start)

N, M, T = map(int, input().split())
board = [[]]
numbersxy = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
for _ in range(N):
    board.append(deque(map(int, input().split())))
for _ in range(T):
    x, d, k = map(int, input().split())
    rotate(x, d, k)
    isfind = False
    visit = [[False] * M for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(M):
            if board[i][j] and not visit[i][j]:
                flag = 0
                num = board[i][j]
                dfs(i, j, num)
                if flag:
                    board[i][j] = 0
    if not isfind:
        SUM = 0
        stack = []
        for i in range(1, N+1):
            for j in range(M):
                if board[i][j]:
                    SUM += board[i][j]
                    stack.append((i, j))

        if len(stack):
            number = SUM / len(stack)
            for x, y in stack:
                if number < board[x][y]:
                    board[x][y] -= 1
                elif number > board[x][y]:
                    board[x][y] += 1


result = 0
for i in range(1, N+1):
    for j in range(M):
        result += board[i][j]
print(result)