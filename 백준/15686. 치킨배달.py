
def back(k, n):
    global result

    if len(select) == M:
        res = 0
        for i in range(len(home)):
            tmp = []
            for j in select:
                tmp.append(dis[i][j])
            res += min(tmp)
        result = min(result, res)
        return

    for i in range(k, n):
        select.append(i)
        back(i+1, n)
        select.pop()


N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
home = []
god = []
select = []
result = 0xfffffff
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            home.append((i, j))
        elif board[i][j] == 2:
            god.append((i, j))
dis = [[] for _ in range(len(home))]
for i in range(len(home)):
    for j in range(len(god)):
        dis[i].append(abs(home[i][0] - god[j][0]) + abs(home[i][1] - god[j][1]))
print(dis)
back(0, len(god))
print(result)