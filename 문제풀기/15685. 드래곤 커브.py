def curve(x, y, d, g):
    start = (x, y)
    end = (x+dx[d], y+dy[d])
    board[x+dx[d]][y+dy[d]] = True
    gcurve = [start, end]
    for _ in range(g):
        tmp = []
        for i in range(len(gcurve)-1, 0, -1):
            curx, cury = gcurve[i]
            nx, ny = gcurve[i-1]
            cdx, cdy = diretion[(nx-curx, ny-cury)]
            endx, endy = end
            end = (endx + cdx, endy + cdy)
            tmp.append(end)
            if -1 < endx+cdx < 101 and -1 < endy+cdy < 101:
                board[endx+cdx][endy+cdy] = True
        gcurve.extend(tmp)

N = int(input())

board = [[False] * 101 for _ in range(101)]
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
for _ in range(N):
    y, x, d, g = map(int, input().split())
    diretion = {(1, 0):(0, -1), (0, -1):(-1, 0), (-1, 0):(0, 1), (0, 1):(1, 0)}
    board[x][y] = True
    curve(x, y, d, g)
result = 0
for i in range(101):
    for j in range(101):
        if -1 < j+1 < 101 and -1 < i+1 < 101 and board[i][j] and board[i+1][j] and board[i][j+1] and board[i+1][j+1]:
            result += 1
print(result)
