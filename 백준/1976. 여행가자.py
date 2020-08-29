def find(x):
    if x == parent[x]:
        return x

    p = find(parent[x])
    parent[x] = p
    return p

def union(a, b):
    x = find(a)
    y = find(b)

    if x != y:
        parent[y] = x

def check(lst):
    if len(lst) < 2:
        return True
    else:
        chk = find(lst[0]-1)
        for i in range(1, len(lst)):
            tmp = find(lst[i]-1)
            if tmp != chk:
                return False
        return True
N = int(input())
M = int(input())

parent = [x for x in range(N)]

for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(N):
        if tmp[j] == 1:
            union(i, j)
plan = list(map(int, input().split()))
if check(plan):
    print('YES')
else:
    print('NO')