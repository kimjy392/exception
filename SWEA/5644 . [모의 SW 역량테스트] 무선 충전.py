T = int(input())
d = [(0, 0), (-1, 0), (0, 1), (1, 0), (0, -1)]
for tc in range(1, T+1):
    M, A = map(int, input().split())
    p1 = [0] + list(map(int, input().split()))
    p2 = [0] + list(map(int, input().split()))
    BC = dict()
    for i in range(A):
        y, x, c, p = map(int, input().split())
        BC[(x-1, y-1)] = [c, p]
    a, b = (0, 0), (9, 9)
    res = 0
    for i in range(M+1):
        a = (a[0] + d[p1[i]][0], a[1] + d[p1[i]][1])
        b = (b[0] + d[p2[i]][0], b[1] + d[p2[i]][1])
        tax, tay = a
        tbx, tby = b
        atmp = []
        btmp = []
        for xbc, ybc in BC:
            c, p = BC[(xbc, ybc)]
            if abs(tax - xbc) + abs(tay - ybc) <= c:
                atmp.append((xbc, ybc, p))
            if abs(tbx - xbc) + abs(tby - ybc) <= c:
                btmp.append((xbc, ybc, p))
        if len(atmp) and not len(btmp):
            tp = 0
            for xbc, ybc, p in atmp:
                if p > tp:
                    tp = p
            res += tp
        elif not len(atmp) and len(btmp):
            tp = 0
            for xbc, ybc, p in btmp:
                if p > tp:
                    tp = p
            res += tp
        elif not len(atmp) and not len(btmp):
            continue
        else:
            tp = 0
            for k in range(len(atmp)):
                ap = atmp[k][2]
                for j in range(len(btmp)):
                    bp = btmp[j][2]
                    if atmp[k] == btmp[j]:
                        if ap > tp:
                            tp = ap
                    else:
                        if ap + bp > tp:
                            tp = ap + bp
            res += tp
    print('#{}'.format(tc), res)
