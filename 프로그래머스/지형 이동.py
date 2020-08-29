def bfs(x, y, visit, maps, group):
    visit[x][y] = group
    stack = [(x, y)]
    while stack:


def solution(land, height):

    N, M = len(land), len(land[0])
    visit = [[0] * M for _ in range(N)]
    answer = 0

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    cnt = 0
    return answer

print(solution([[10, 11, 10, 11], [2, 21, 20, 10], [1, 20, 21, 11], [2, 1, 2, 1]], 1))
