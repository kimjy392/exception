def addzero(lst, n):
    max_len = 0
    for i in range(n):
        if len(lst[i]) > max_len:
            max_len = len(lst[i])
    if max_len > 100:
        max_len = 100
    for i in range(n):
        if len(lst[i]) > max_len:
            lst[i] = lst[i][:100]
            continue
        lst[i] += [0] * (max_len - len(lst[i]))
    return lst

def cal(lst):
    tmp = set()
    for i in range(len(lst)):
        if lst[i] == 0: continue;
        tmp.add((lst.count(lst[i]), lst[i]))
    tmp = sorted(list(tmp))
    if len(tmp) > 100:
        tmp = tmp[:100]
    res = []
    for count, num in tmp:
        res.extend([num, count])
    return res

r, c, k = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(3)]
result = 0
flag = 0
for time in range(0, 101):
    if -1 < r - 1 < len(A) and -1 < c - 1 < len(A[0]) and A[r-1][c-1] == k:
        result = time
        flag = 1
        break

    tmp = []
    if len(A) >= len(A[0]): # 행이 많을 때
        for R in A:
            tmp.append(cal(R))
        A = addzero(tmp, len(tmp))

    else:   # 열이 많을 때
        for y in range(len(A[0])):
            stk = []
            for x in range(len(A)):
                stk.append(A[x][y])
            tmp.append(cal(stk))
        Atmp = addzero(tmp, len(tmp))
        A = [[0] * len(Atmp) for _ in range(len(Atmp[0]))]
        for y in range(len(A[0])):
            for x in range(len(A)):
                A[x][y] = Atmp[y][x]


if flag:
    print(result)
else:
    print(-1)