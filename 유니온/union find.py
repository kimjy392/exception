def make_set(x):
    return [x for x in range(x+1)]

def union(x, y, parent):
    yroot = find(y, parent)
    xroot = find(x, parent)
    parent[yroot] = xroot
    print(parent, x ,y)

def find(x, parent):
    if x == parent[x]:
        return parent[x]
    return find(parent[x], parent)

parent = make_set(8)
union(1, 2, parent)
union(4, 5, parent)
union(6, 1, parent)
union(3, 7, parent)
union(7, 8, parent)
union(2, 5, parent)

