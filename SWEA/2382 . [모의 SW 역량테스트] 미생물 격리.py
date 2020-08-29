import copy

T = int(input())
dt = [(-1, 0), (1, 0), (0, -1), (0, 1)]
change = {0:1, 1:0, 2:3, 3:2}
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    tiny = dict()
    for _ in range(K):
        x, y, ea, d = map(int, input().split())
        tiny[(x, y)] = [ea, d-1]
    for _ in range(M):
        ttiny = dict()
        tmp = dict()
        for x, y in tiny:
            ea, d = tiny[(x, y)]
            tx, ty = x + dt[d][0], y + dt[d][1]
            if (tx, ty) in ttiny:
                nea, nd = ttiny[(tx, ty)]
                if nea > ea:
                    ttiny[(tx, ty)] = [nea, nd]
                else:
                    ttiny[(tx, ty)] = [ea, d]
                if tmp.get((tx, ty)):
                    tmp[(tx, ty)].append(ea)
                else:
                    tmp[(tx, ty)] = [ea, nea]
            elif ty == 0 or ty == N-1 or tx == 0 or tx == N - 1:
                td = change[d]
                tea = ea // 2
                ttiny[(tx, ty)] = [tea, td]
            else:
                ttiny[(tx, ty)] = [ea, d]
        for x, y in tmp:
            ttiny[(x, y)][0] = sum(tmp[(x, y)])
        tiny = copy.copy(ttiny)
    result = 0
    for ea, d in tiny.values():
        result += ea
    print('# {} {}'.format(tc, result))

