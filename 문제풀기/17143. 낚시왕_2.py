def move(x, y):
    s, d, z = sharks[(x, y)]
    tx, ty = x, y
    if d == 1 or d == 2:
        for i in range(s%((R-1)*2)):
            if d == 1 and tx == 0:
                d = 2
            elif d == 2 and tx == R-1:
                d = 1
            tx += dx[d]
    elif d == 3 or d == 4:
        for i in range(s % ((C - 1) * 2)):
            if d == 3 and ty == C-1:
                d = 4
            elif d == 4 and ty == 0:
                d = 3
            ty += dy[d]
    return (tx, ty, s, d, z)

R, C, M = map(int, input().split())
sharks = dict()
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    sharks[(r-1, c-1)] = [s, d, z]
dx = [0, -1, 1]
dy = [0, 0, 0, 1, -1]
result = 0
for i in range(C):
    for j in range(R):
        if sharks.get((j, i)):
            result += sharks.get((j, i))[2]
            del sharks[(j, i)]
            break
    tmp = dict()
    for key in sharks:
        newshark = move(key[0], key[1])
        if newshark:
            if tmp.get((newshark[0], newshark[1])):
                if tmp.get((newshark[0], newshark[1]))[2] > newshark[4]:
                    continue
                else:
                    tmp[(newshark[0], newshark[1])] = [newshark[2], newshark[3], newshark[4]]
            else:
                tmp[(newshark[0], newshark[1])] = [newshark[2], newshark[3], newshark[4]]

    sharks.clear()
    sharks.update(tmp)
print(result)