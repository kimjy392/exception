import sys
sys.setrecursionlimit(10**6)
def solution(n, edge):
    answer = 0
    G = [[] for _ in range(n+1)]
    for e in edge:
        u, v = e
        G[u].append(v)
        G[v].append(u)
    visit = [1e9] * (n+1)
    visit[1] = 0
    stack = [(1, 0)]
    while stack:
        print(stack)
        node, res = stack.pop(0)
        for n in G[node]:
            if res + 1 < visit[n]:
                visit[n] = res + 1
                stack.append((n, res + 1))
    return answer

solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])