def move(x, y):
    d = sharks[(x, y)][1]
    s = sharks[(x, y)][0]
    z = sharks[(x, y)][2]
    if d == 1:
        if x >= s:
            if nextsharks.get((x-s, y)) == None:
                nextsharks[(x-s, y)] = sharks[(x, y)]
            else:
                if nextsharks[(x-s, y)][2] > z:
                    return
                else:
                    nextsharks[(x - s, y)] = sharks[(x, y)]
        else:
            ts = s - x
            q = ts // (R-1)
            r = ts % (R-1)
            if q % 2: # 방향 바뀜
                if nextsharks.get((R-1-r, y)) == None:
                    nextsharks[(R-1-r, y)] = (s, 1, z)
                else:
                    if nextsharks[(R - 1 - r, y)][2] > z:
                        return
                    else:
                        nextsharks[(R - 1 - r, y)] = (s, 1, z)
            else: # 방향 안바뀜
                if nextsharks.get((r, y))== None:
                    nextsharks[(r, y)] = (s, 2, z)
                else:
                    if nextsharks[(r, y)][2] > z:
                        return
                    else:
                        nextsharks[(r, y)] = (s, 2, z)
    elif d == 2:
        if R-1 - x >= s: # 아직 큰상어로 바꾸진 않았으
            if nextsharks.get((x+s, y)) == None:
                nextsharks[(x+s, y)] = sharks[(x, y)]
            else:
                if nextsharks[(x+s, y)][2] > z:
                    return
                else:
                    nextsharks[(x + s, y)] = sharks[(x, y)]
        else:
            ts = s - (R-1-x)
            q = ts // (R-1)
            r = ts % (R-1)
            if q % 2: # 방향이 바뀜
                if nextsharks.get((r, y)) == None:
                    nextsharks[(r, y)] = (s, 2, z)
                else:
                    if nextsharks[(r, y)][2] > z:
                        return
                    else:
                        nextsharks[(r, y)] = (s, 2, z)
            else: # 방향이 안바뀜
                if nextsharks.get((R-1-r, y)) == None:
                    nextsharks[(R-1-r, y)] = (s, 1, z)
                else:
                    if nextsharks[(R-1-r, y)][2] > z:
                        return
                    else:
                        nextsharks[(R - 1 - r, y)] = (s, 1, z)

    elif d == 3:
        if C-1 - y >= s:
            if nextsharks.get((x, y+s)) == None:
                nextsharks[(x, y + s)] = sharks[(x, y)]
            else:
                if nextsharks[(x, y + s)][2] > z:
                    return
                else:
                    nextsharks[(x, y + s)] = sharks[(x, y)]
        else:
            ts = s - (C - 1 - y)
            q = ts // (C - 1)
            r = ts % (C - 1)
            if q % 2:
                if nextsharks.get((x, r)) == None:
                    nextsharks[(x, r)] = (s, 3, z)
                else:
                    if nextsharks[(x, r)][2] > z:
                        return
                    else:
                        nextsharks[(x, r)] = (s, 3, z)
            else:
                if nextsharks.get((x, C - 1 - r)) == None:
                    nextsharks[(x, C - 1 - r)] = (s, 4, z)
                else:
                    if nextsharks[(x, C - 1 - r)][2] > z:
                        return
                    else:
                        nextsharks[(x, C - 1 - r)] = (s, 4, z)

    elif d == 4:
        if y >= s:
            if nextsharks.get(((x, y - s))) == None:
                nextsharks[(x, y - s)] = sharks[(x, y)]
            else:
                if nextsharks[(x, y - s)][2] > z:
                    return
                else:
                    nextsharks[(x, y - s)] = sharks[(x, y)]
        else:
            ts = s - y
            q = ts // (C - 1)
            r = ts % (C - 1)
            if q % 2:  # 방향 바뀜
                if nextsharks.get((x, C - 1 - r)) == None:
                    nextsharks[(x, C - 1 - r)] = (s, 4, z)
                else:
                    if nextsharks[(x, C - 1 - r)][2] > z:
                        return
                    else:
                        nextsharks[(x, C - 1 - r)] = (s, 4, z)
            else:  # 방향 안바뀜
                if nextsharks.get((x, r)) == None:
                    nextsharks[(x, r)] = (s, 3, z)
                else:
                    if nextsharks[(x, r)][2] > z:
                        return
                    else:
                        nextsharks[(x, r)] = (s, 3, z)

R, C, M = map(int, input().split())
sharks = dict()
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    sharks[(r-1,c-1)] = (s, d, z)
state = 0 # 사람 위치
nextsharks = dict()
result = 0
for key in sharks:
    move(key[0], key[1])
while state < C:
    for i in range(R):
        if sharks.get((i, state)) != None:
            result += sharks[(i, state)][2]
            del sharks[(i, state)]
            break
    nextsharks = dict()
    for key in sharks:
        move(key[0], key[1])
    sharks.clear()
    sharks.update(nextsharks)
    state += 1
print(result)
# 사람위치를 하니씩 변화시키면서
# 세로로 반복문 돌면서 가장 가까운 곳을 찾는다
# 딕셔너리 get() 함수 이용,-1 이면 넘기고 있으면 결과에 추가하고 키를 삭제한다.
# 상어를 이동시킨다. 상어를 이동시킬 때는 shark 변수를 다시 만든다.
# 이동시킨 상어가 마지막라인이라면 방향을 바꾸고 저장
# 상어를 이동시키는 도중 이동 위치에 상어가 있다면 큰상어로 바꾼다.
# 위를 반복한다.
