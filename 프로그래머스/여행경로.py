from copy import deepcopy

def solution(tickets):
    answer = []
    visit = dict()
    where = dict()
    for ticket in tickets:
        a, b = ticket
        if where.get(a):
            where[a].append(b)
            visit[a].append(0)
            where[a].sort()
        else:
            where[a] = [b]
            visit[a] = [0]
    answer.append('ICN')
    stack = [('ICN', visit, ['ICN'])]
    while stack:
        airport, visit, result = stack.pop(0)
        if len(result) > len(answer):
            answer = result
        if not where.get(airport):
            continue
        for idx, goairport in enumerate(where[airport]):
            if not visit[airport][idx]:
                visit[airport][idx] = 1
                result.append(goairport)
                stack.append((goairport, deepcopy(visit), result[:]))
                visit[airport][idx] = 0
                result.pop()
    return answer


print(solution([['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL','SFO']]))