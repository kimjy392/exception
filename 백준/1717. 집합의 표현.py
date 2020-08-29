import sys
def find(x):
    if x == parent[x]:
        return x
    p = find(parent[x])
    parent[x] = p
    return p

def union(num1, num2, o):
    x = find(num1)
    y = find(num2)
    if o:
        if x == y:
            print('YES')
        else:
            print('NO')
        return
    if x != y:
        parent[y] = x

n, m = map(int, sys.stdin.readline().split())
parent = [x for x in range(n+1)]

for _ in range(m):
    c, a, b = map(int, sys.stdin.readline().split())
    union(a, b, c)


# parent = [0, 1, 1, 2, 4, 5]
# a = 3
# while a != parent[a]:
#     a = parent[a]
#