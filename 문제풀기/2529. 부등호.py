def back(depth, n):
    global MAX, MIN
    if depth == n:
        tmp = ''.join(sel)
        if int(tmp) > int(MAX):
            MAX = tmp
        if int(tmp) < int(MIN):
            MIN = tmp
        return

    for i in range(10):
        if signs[depth] == '<':
            if int(sel[-1]) < i and not select[i]:
                select[i] = True
                sel.append(str(i))
                back(depth+1, k)
                sel.pop()
                select[i] = False
        else:
            if int(sel[-1]) > i and not select[i]:
                select[i] = True
                sel.append(str(i))
                back(depth+1, k)
                sel.pop()
                select[i] = False
k = int(input())

signs = list(input().split())
select = [False] * 10
sel = []
MAX , MIN = 0, 10**15
for i in range(0, 10):
    select[i] = True
    sel.append(str(i))
    back(0, k)
    sel.pop()
    select[i] =  False
print(MAX)
print(MIN)