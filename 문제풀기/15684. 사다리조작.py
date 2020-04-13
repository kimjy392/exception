def dfs(x, y, ex, ey, py):
    global check
    if x == 2*H-2 and y == py:
        check += 1
        return

    for dx, dy in [(0, 1), (0, -1), (1, 0)]:
        tx = x + dx
        ty = y + dy
        if -1 < tx < 2*H-1 and -1 < ty < 2*N-1 and (tx, ty) != (ex, ey) and ladders[tx][ty] == 1:
            dfs(tx, ty, x, y, py)
            break

def back(k, n, sx):
    global result, check
    if k == n:
        # print(line)
        for i in range(M, len(line)):
            ladders[line[i][0]][line[i][1]] = 1
        check = 0
        for i in range(N):
            dfs(0, 2*i, 0, 2*i, 2*i)
        if check == N:
            if result > n:
                result = n
        for i in range(M, len(line)):
            ladders[line[i][0]][line[i][1]] = 0
        return
    for x in range(sx, H):
        for y in range(N-1):
            if (2*x, 2*y+1) not in line:
                for dx, dy in [(0, 2), (0, -2)]:
                    tx = 2*x + dx
                    ty = 2*y + 1 + dy
                    if -1 < tx < 2*H-1 and -1 < ty < 2*N-1 and (tx, ty) in line:
                        break
                else:
                    line.append((2*x, 2*y+1))
                    back(k+1, n, x)
                    line.pop()



N, M, H = map(int, input().split())
ladders = [ [0]*(2*N-1) for _ in range(2*H-1)]
line = []
for _ in range(M):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    ladders[2*a][2*b+1] = 1
    line.append((2*a, 2*b+1))
# 짝수만 선을 놓을 수 있게
# 세로 짝수가 선을 의미
# 세로는 홀수가 선을 놓을 수 있게
for i in range(2*H-1):
    for j in range(2*N):
        if j % 2 == 0:
            ladders[i][j] = 1
result = 0xffff
for i in range(0, 4):
    if result != 0xffff:
        break
    back(0, i, 0)
if result == 0xffff:
    print(-1)
else:
    print(result)
# 10 5 30
# 30 9
# 3 2
# 2 3
# 5 1
# 5 4