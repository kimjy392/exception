from copy import deepcopy

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    atoms = dict()
    for _ in range(N):
        y, x, d, e = map(int, input().split())
        atoms[(2000 - (1000+x), 1000+y)] = [(d, e)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    result = 0

    for i in range(2001):
        delete = []
        tmp = dict()
        if atoms:
            for key, value in atoms.items():
                x, y = key
                d, e = value[0]
                tx, ty = x + dx[d], y + dy[d]
                if atoms.get((tx, ty)):
                    if (d == 0 and atoms[(tx, ty)][0][0] == 1) or (d == 1 and atoms[(tx, ty)][0][0] == 0):
                        result += e
                        continue
                    elif (d == 2 and atoms[(tx, ty)][0][0] == 3) or (d == 3 and atoms[(tx, ty)][0][0] == 2):
                        result += e
                        continue
                if tmp.get((tx, ty)):
                    tmp.get((tx, ty)).append((d, e))
                else:
                    tmp[(tx, ty)] = [(d, e)]
        else:
            break
        if tmp:
            for key, value in tmp.items():
                x, y = key
                if len(value) > 1:
                    for val in value:
                        result += val[1]
                    delete.append((x, y))
            if delete:
                for de in delete:
                    del tmp[de]
            atoms.clear()
            for key, value in tmp.items():
                atoms[key] = value
        else:
            break
    print('#{} {}'.format(tc, result))

