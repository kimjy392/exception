def hor(x, y, candy):
    global ans
    for i in range(x, N):
        if board[i][y] == candy:
            ans += 1
        else:
            break
    for i in range(x- 1, -1, -1):
        if board[i][y] == candy:
            ans += 1
        else:
            break

def ver(x, y, candy):
    global ans
    for i in range(y, N):
        if board[x][i] == candy:
            ans += 1
        else:
            break
    for i in range(y-1, -1, -1):
        if board[x][i] == candy:
            ans += 1
        else:
            break


N = int(input())

board = [list(input()) for _ in range(N)]
direction = [(1, 0), (0, 1)]
result = 0
for i in range(N):
    for j in range(N):
        for d in direction:
            dx, dy = d
            tx, ty = i + dx, j + dy
            if -1 < tx < N and -1 < ty < N:
                board[i][j], board[tx][ty] = board[tx][ty], board[i][j]
                ans = 0
                hor(i, j, board[i][j])
                if ans > result:
                    result = ans
                ans = 0
                ver(i, j, board[i][j])
                if ans > result:
                    result = ans
                board[i][j], board[tx][ty] = board[tx][ty], board[i][j]
print(result)
