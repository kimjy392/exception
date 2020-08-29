def solution(N, road, K):
    answer = 0
    G = [[] for _ in range(N + 1)]
    times = [[] for _ in range(N + 1)]
    for ro in road:
        ex, ne, time = ro
        G[ex].append(ne)
        G[ne].append(ex)
        times[ne].append(time)
        times[ex].append(time)
    print(G)
    print(times)

    def bfs(n):
        visit = [1e9] * (n+1)
        visit[1] = 0
        stack = [(1, 0)]
        while stack:
            u, time = stack.pop(0)
            for idx, g in enumerate(G[u]):
                if time + times[u][idx] < visit[g] and time + times[u][idx] <= K:
                    visit[g] = time + times[u][idx]
                    stack.append((g, time + times[u][idx]))
        result = 0
        for i in visit:
            if i != 1e9:
                result += 1
        return result

    answer = bfs(N)

    return answer

solution(5	,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],	3)