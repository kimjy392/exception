def solution(n, path, order):
    answer = True
    visit = [0] * n
    G = [[] for _ in range(n)]
    for a, b in path:
        G[a].append(b)
        G[b].append(a)
    isgo = [0] * n
    nex = [0] * n
    for a, b in order:
        isgo[b] = a
    def dfs(x):
        if visit[x]:
            return
        if not visit[isgo[x]]:
            nex[isgo[x]] = x
            return

        visit[x] = True
        if nex[x]:
            dfs(nex[x])
        for g in G[x]:
            dfs(g)
    if isgo[0]:
        return False
    visit[0] = 1
    for i in G[0]:
        dfs(i)
    if sum(visit) == n:
        return True
    else:
        return False
    return answer

print(solution(9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[8,5],[6,7],[4,1]]))