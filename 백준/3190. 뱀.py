from collections import deque
N = int(input())
board = [[0] * N for _ in range(N)]
K = int(input())
for _ in range(K):
    x, y = map(int ,input().split())
    board[x-1][y-1] = 1
L = int(input())
X = [0] * 10001
for _ in range(L):
    x, d = input().split()
    X[int(x)] = d
# 동 0, 서 1, 남 2, 북 3
di = {
    0: {'L': 3, 'D': 2},
    1: {'L': 2, 'D': 3},
    2: {'L': 0, 'D': 1},
    3: {'L': 1, 'D': 0}
    }
# 전진 방향
go = [(0, 1), (0, -1), (1, 0), (-1, 0)]

snake = deque([(0, 0)])
d = 0
time = 0

while True:
    visit = [[False] * N for _ in range(N)]
    if X[time]:
        d = di[d][X[time]]
    x, y = snake[0]
    dx, dy = go[d]
    tx = x + dx
    ty = y + dy
    time += 1
    if -1 < tx < N and -1 < ty < N:
        if (tx, ty) not in snake:
            snake.appendleft((tx,ty))
            if board[tx][ty] == 0:
                snake.pop()
        else:
            break
    else:
        break

    print(time)
    for a, b in snake:
        visit[a][b] = True
    for z in board:
        print(z)
    print('----------------')
    for c in visit:
        print(c)
    print()

print(time)