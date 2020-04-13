def back(k, n, res):
    if k == n:
        print(res)
        return

    AB = []
    BB = []
    for bettery in BC:
        x, y, d, P = bettery
        for idx, user in enumerate(users):
            ux, uy = user
            distance = abs(x - ux) + abs(y - uy)
            if distance <= d:
                if not idx:
                    AB.append(idx)
                else:
                    BB.append(idx)

    for idx in range(len(users)):
        x, y  = users[idx]
        tx, ty = x, y
        if not idx:
            tx += dx[Aroad[k]]
            ty += dy[Aroad[k]]
        else:
            tx += dx[Broad[k]]
            ty += dy[Broad[k]]
        users[idx] = [tx, ty]
    ABC.append(AB)
    BBC.append(BB)
    allBC.append()

T = int(input())

for tc in range(1, T+1):
    M, A = map(int ,input().split())
    Aroad = list(map(int, input().split()))
    Broad = list(map(int, input().split()))
    BC = [list(map(int, input().split())) for _ in range(A)]
    users = [[0, 0], [9, 9]]
    dx = [0, -1, 0, 1, 0]
    dy = [0, 0, 1, 0, -1]
    ABC = []
    BBC = []
    allBC = []
    back(0, M, 0)