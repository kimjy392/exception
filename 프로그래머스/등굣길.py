def solution(m, n, puddles):
    answer = 0
    board = [[0] * n for _ in range(m)]
    for x, y, in puddles:
        board[x - 1][y - 1] = -1
    board[0][0] = 1
    d = [(-1, 0), (0, -1)]
    for i in range(m):
        for j in range(n):
            if board[i][j] == -1 or (i==0 and j== 0):
                continue
            tmp = 0
            for dx, dy in d:
                tx, ty = i + dx, j + dy
                if -1 < tx < m and -1 < ty < n and board[tx][ty] != -1:
                    tmp += board[tx][ty]
            board[i][j] = tmp

    return board[m-1][n-1]

solution(4, 3, [[2, 2]])