from sys import stdin
input = stdin.readline

def find(x):
    if x == parent[x]:
        parent[x] = x
        return x
    p = find(parent[x])
    parent[x] = p
    return p

def union(a, b):
    x = find(a)
    y = find(b)

    if x != y:
        parent[y] = x

G = int(input())
P = int(input())

parent = [x for x in range(G+1)]
count = 0
for _ in range(P):
    plane = int(input())
    plane = find(plane)
    if plane:
        union(plane-1, plane)
        count += 1
    else:
        break

print(count)