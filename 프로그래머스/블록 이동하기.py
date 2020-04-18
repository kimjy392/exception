def bfs(boar):
    x1, y1, x2, y2 = 0, 0, 0, 1
    stack = [(0, 0, 0, 1, 0)]
    dvisit = [[0] * M for _ in range(N)]
    res = 99999
    while stack:
        x1, y1, x2, y2, d = stack.pop(0)
        if d > res:
            continue
        if (x1, y1) == (N-1, M-1) or (x2, y2) == (N-1, M-1):
            if res > d:
                res = d
                continue
        model = (abs(x1 - x2), abs(y1 - y2))
        for idx, direction in enumerate(isrotate.get(model)):
            dx1, dy1, dx2, dy2 = direction
            tx1, ty1, tx2, ty2 = x1 + dx1, y1 + dy1, x2 + dx2, y2 + dy2
            if -1 < tx1 < N and -1 < ty1 < M and -1 < tx2 < N and -1 < ty2 < M and not boar[tx1][ty1] and not boar[tx2][ty2] and not visit.get((tx1, ty1, tx2, ty2)):
                nx1, ny1, nx2, ny2 = rotate[model][idx]
                tmp = [(x1+nx1, y1+ny1), (x2+nx2, y2+ny2)]
                tmp.sort()
                visit[(tmp[0][0], tmp[0][1], tmp[1][0], tmp[1][1])] = True
                stack.append((tmp[0][0], tmp[0][1], tmp[1][0], tmp[1][1], d+1))
        for direction in move:
            dx1, dy1, dx2, dy2 = direction
            tx1, ty1, tx2, ty2 = x1 + dx1, y1 + dy1, x2 + dx2, y2 + dy2
            if -1 < tx1 < N and -1 < ty1 < M and -1 < tx2 < N and -1 < ty2 < M and not boar[tx1][ty1] and not boar[tx2][ty2] and not visit.get((tx1, ty1, tx2, ty2)):
                stack.append((tx1, ty1, tx2, ty2, d+1))
                visit[(tx1, ty1, tx2, ty2)] = True

    return res


def solution(board):
    global visit, N, M, isrotate, rotate, move
    answer = 0
    visit = dict()
    visit[(0, 0, 0, 1)] = True
    N, M = len(board), len(board[0])
    rotate = {
        (0, 1): [(1, 1, 0, 0), (-1, 1, 0, 0), (0, 0, 1, -1), (0, 0, -1, -1)],
        (1, 0): [(1, 1, 0, 0), (1, -1, 0, 0), (0, 0, -1, 1), (0, 0, -1, -1)]
    }
    isrotate = {
        (0, 1): [(1, 0, 1, 0), (-1, 0, -1, 0), (1, 0, 1, 0), (-1, 0, -1, 0)],
        (1, 0): [(0, 1, 0, 1), (0, -1, 0, -1), (0, 1, 0, 1), (0, -1, 0, -1)]
    }
    move = [(0, 1, 0, 1), (0, -1, 0, -1), (1, 0, 1, 0), (-1, 0, -1, 0)]
    answer = bfs(board)
    return answer

print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))