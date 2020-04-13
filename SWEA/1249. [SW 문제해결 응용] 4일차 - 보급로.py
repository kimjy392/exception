from collections import deque

def bfs(x, y):
    visit[x][y] = 0
    stack = deque([(x, y)])
    while stack:
        x, y = stack.popleft()
        for dx, dy in (1, 0), (-1, 0), (0, 1):
            nx, ny = x + dx, y + dy
            if -1 < nx < N and -1 < ny < N and visit[nx][ny] > visit[x][y] + board[nx][ny]:
                visit[nx][ny] = visit[x][y] + board[nx][ny]
                stack.append((nx, ny))

    return visit[N-1][N-1]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, input())) for _ in range(N)]
    visit = [[N*N*9] * N for _ in range(N)]
    print('#{} {}'.format(tc, bfs(0, 0)))