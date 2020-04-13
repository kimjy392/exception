from collections import deque

def rotate(magnetic, direction):
    if direction == 1:
        tmp = gears[magnetic].pop()
        gears[magnetic].appendleft(tmp)
    elif direction == -1:
        tmp = gears[magnetic].popleft()
        gears[magnetic].append(tmp)

def cal(curmag, exmag, flow):
    curmagcheck = 6
    exmagcheck = 2
    if flow == 1:
        curmagcheck = 2
        exmagcheck = 6

    if gears[curmag][curmagcheck] != gears[exmag][exmagcheck]:
        if magdirection[exmag] == 1:
            magdirection[curmag] = -1
        else:
            magdirection[curmag] = 1
        return 0
    return 1


T = int(input())

for tc in range(1, T+1):
    K = int(input())
    gears = [deque(list(map(int, input().split()))) for _ in range(4)]
    result = 0
    for _ in range(K):
        mag, direction = map(int, input().split())
        mag -= 1
        magdirection = [0] * 4
        magdirection[mag] = direction
        for curmagidx in range(mag-1, -1, -1):
            exmagidx = curmagidx + 1
            if cal(curmagidx, exmagidx, 1):
                break
        for curmagidx in range(mag+1, 4):
            exmagidx = curmagidx - 1
            if cal(curmagidx, exmagidx, 0):
                break
        for ro in range(4):
            rotate(ro, magdirection[ro])
    for idx, mag in enumerate(gears):
        if mag[0] == 1:
            result += 2 ** idx

    print('#{} {}'.format(tc, result))