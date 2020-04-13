def move(k, n):
    global result, coins
    if k == n or k >= result:
        return

    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        tmp = []
        cnt = 0
        for i in range(2):
            coin = coins[i]
            tmp.append(coin)
            tx = coin[0] + dx
            ty = coin[1] + dy
            if -1 < tx < N and -1 < ty < M:
                if board[tx][ty] == 0:
                    coins[i] = (tx,ty)
            else:
                coins[i] = (tx, ty)
                cnt += 1
        if tmp == coins or cnt == 2:
            coins = tmp
            continue
        elif cnt == 1:
            result = k
            return
        else:
            move(k+1, n)
        coins = tmp



N, M = map(int, input().split())
board = []
coins = []
result = 11
for j in range(N):
    tmp = list(input())
    for i in range(len(tmp)):
        if tmp[i] == 'o':
            tmp[i] = 0
            coins.append([j, i])
        elif tmp[i] == '#':
            tmp[i] = 2
        else:
            tmp[i] = 0

    board.append(tmp)
move(1, 11)
if result == 11:
    print(-1)
else:
    print(result)