import sys
def find(x):
    if friend.get(x) == x:
        return x
    parent = find(friend[x])
    friend[x] = parent
    return parent

def union(f1, f2):
    x = find(f1)
    y = find(f2)

    if x != y:
        friend[y] = x
        cfriend[x] = cfriend[x] + cfriend[y]
        del cfriend[y]

T = int(input())

for _ in range(T):
    F = int(input())
    friend = dict()
    cfriend = dict()
    for i in range(F):
        a, b = sys.stdin.readline().split()
        if not friend.get(a):
            friend[a] = a
            cfriend[a] = 1
        if not friend.get(b):
            friend[b] = b
            cfriend[b] = 1
        union(a, b)
        print(cfriend[find(a)])
