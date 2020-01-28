def dfs(x, y, k, n):
    global result
    visit[x][y] = True
    if k == n:
        return
    cur = board[x][y]
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if not ismove[cur][i] or tx < 0 or tx > N - 1 or ty < 0 or ty > M - 1:
            continue
        if board[tx][ty] in direction[i] and not visit[tx][ty]:
            result += 1
            dfs(tx, ty, k+1, n)

T = int(input())

for tc in range(1, T+1):
    N, M, R, C, time = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    # 동 0 서 1 남 2 북 3
    direction = {
            0: [1, 3, 6, 7],
            1: [1, 3, 4, 5],
            2: [1, 2, 4, 7],
            3: [1, 2, 5, 6]
        }
    ismove = {
        1: [True, True, True, True],
        2: [False, False, True, True],
        3: [True, True, False, False],
        4: [True, False, False, True],
        5: [True, False, True, False],
        6: [False, True, True, False],
        7: [False, True, False, True]
    }
    result = 1
    visit = [[False] * M for _ in range(N)]
    dx = [0 ,0, 1, -1]
    dy = [1, -1, 0, 0]
    dfs(R, C, 1, time)
    print('#{} {}'.format(tc, result))