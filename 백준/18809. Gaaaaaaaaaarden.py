def rcom(s, n, dep):
    global result
    if n == dep:
        visit2 = [[('', -1)] * M for _ in range(N)]
        stack = Gmed + Rmed
        for tu in stack:
            x, y, _, c = tu
            visit2[x][y] = (c, 0)
        res = 0
        ex = {}
        while stack:
            x, y, time, color = stack.pop(0)
            if ex.get((x, y)):
                continue
            for dx, dy in move:
                tx, ty = x + dx, y + dy
                if -1 < tx < N and -1 < ty < M and garden[tx][ty] != 0:
                    vcolor, vtime = visit2[tx][ty]
                    if vtime == -1:
                        visit2[tx][ty] = (color, time+1)
                        stack.append((tx, ty, time+1, color))
                    elif vcolor != color and vtime == time+1:
                        visit2[tx][ty] = ('f', time+1)
                        ex[(tx, ty)] = True
                    elif vcolor == 'f':
                        continue

        for i in range(N):
            for j in range(M):
                c, _ = visit2[i][j]
                if c == 'f':
                    res += 1
        if result < res:
            result = res
        return

    for i in range(s, len(lands)):
        if not visit[i]:
            Rmed.append((lands[i]) + ['r'])
            rcom(i+1, n+1, dep)
            Rmed.pop()

def com(s, n, dep):
    if n == dep:
        rcom(0, 0, R)
        return

    for i in range(s, len(lands)):
        visit[i] = True
        Gmed.append(lands[i] + ['g'])
        com(i+1, n+1, dep)
        visit[i] = False
        Gmed.pop()


N, M, G, R = map(int, input().split())
garden = [list(map(int, input().split())) for _ in range(N)]
lands = []
Gmed = []
Rmed = []
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for i in range(N):
    for j in range(M):
        if garden[i][j] == 2:
            lands.append([i, j, 0])
visit = [False] * len(lands)
result = 0
com(0, 0, G)
print(result)
# 심을 수 있는 곳에서 초록색을 우선 뽑고, 나머지 곳에서 빨간색을 뽑는다.
# 그리고 시뮬레이션을 진행