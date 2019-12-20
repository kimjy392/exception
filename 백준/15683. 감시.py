def back(k, n):
    global result, res
    if k == n:
        tmp = 0
        for i in range(N):
            for j in range(M):
                if not visit[i][j]:
                    tmp += 1
        tmp -= result
        if tmp < res:
            res = tmp
        return

    for di in ran[cctvs[k][2]]: # k 번째 cctv 에서 방향마다
        tmp = []
        x, y = cctvs[k][0], cctvs[k][1]
        visit[x][y] = True
        for dx, dy in di:
            tx = x + dx
            ty = y + dy
            while -1 < tx < N and -1 < ty < M and board[tx][ty] < 6:
                if visit[tx][ty]:
                    tx += dx
                    ty += dy
                    continue
                else:
                    visit[tx][ty] = True
                    tmp.append((tx, ty))
                tx += dx
                ty += dy

        back(k+1, n)
        for i, j in tmp:
            visit[i][j] = False

N, M = map(int, input().split())
board = [list(map(int ,input().split())) for _ in range(N)]
ran = [[],
    [[(0, 1)], [(0, -1)], [(1, 0)], [(-1, 0)]], # cctv 1 번이 4방향을 바라볼때
    [[(0, 1), (0, -1)], [(1, 0), (-1, 0)]],     # cctv 2 번이 2 방향을 바라볼때
    [[(0, 1), (1, 0)], [(0, 1), (-1, 0)], [(0, -1), (1, 0)], [(0, -1), (-1, 0)]], # cctv 3번이 4방향
    [[(0, 1), (0, -1), (-1, 0)], [(-1, 0), (0, 1), (1, 0)], [(0, 1), (1, 0), (0, -1)], [(-1, 0), (0, -1), (1, 0)]],
    [[(0, 1), (0, -1), (1, 0), (-1, 0)]]
]
result = 0
res = 0xffffff
cctvs = []
for i in range(N):
    for j in range(M):
        if 0 < board[i][j] < 6:
            cctvs.append((i, j, board[i][j]))
        if board[i][j] == 6:
            result += 1
visit = [[False] * M for _ in range(N)]
back(0, len(cctvs))
print(res)
