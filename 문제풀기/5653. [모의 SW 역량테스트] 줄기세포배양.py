T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    allcells = dict()
    inactive = dict()
    soondead = dict()
    active = dict()
    dead = dict()
    for i in range(N):
        tmp = list(map(int, input().split()))
        for j in range(M):
            if tmp[j] > 0:
                inactive[(i, j)] = (tmp[j], 0)
                allcells[(i, j)] = 1
    time = 0
    while 1:
        tmp = dict()
        for key, value in soondead.items():
            deadtime = value
            if deadtime == time:
                dead[key] = 1
                tmp[key] = 1
        for key in tmp:
            del soondead[key]
        if time == K:
            break
        tmp.clear()
        for key, value in inactive.items():
            life, created_time = value
            if time - life == created_time:
                tmp[key] = value
        for key, value in tmp.items():
            del inactive[key]
            life, _ = value
            active[key] = life
        for key, value in active.items():
            x, y = key
            life = value
            for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
                tx, ty = x+dx, y+dy
                if allcells.get((tx, ty)):
                    continue
                elif allcells.get((tx, ty)) and inactive.get((tx, ty)):
                    exlife, extime = inactive[(tx, ty)]
                    if exlife < life:
                        inactive[(tx, ty)] = (life, extime)
                else:
                    inactive[(tx, ty)] = (life, time+1)
                    allcells[(tx, ty)] = 1
            soondead[(x, y)] = time+life
        active.clear()
        time += 1
    print('#{} {}'.format(tc, len(inactive)+len(soondead)))

