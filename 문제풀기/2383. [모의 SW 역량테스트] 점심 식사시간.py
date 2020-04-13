def back(k, n):
    if k == n:
        global result
        wait = [[], []]
        down = [[], []]
        rest = []
        time = 0
        while 1:
            if result <= time:
                break
            if len(rest) == len(people):
                result = min(time, result)
            time += 1
            for key, value in select.items():
                stair, movetime = value
                if movetime == time:
                    wait[stair].append(time)
            for i in range(2):
                cnt = 0
                for j in range(len(down[i])):
                    if down[i][j] == time:
                        cnt += 1
                for _ in range(cnt):
                    rest.append(down[i].pop(0))
                cnt = 0
                for j in range(len(wait[i])):
                    if wait[i][j] < time and len(down[i]) < 3:
                        cnt += 1
                        down[i].append(time+board[stairs[i][0]][stairs[i][1]])
                for _ in range(cnt):
                    wait[i].pop(0)
        return
    select[people[k]] = (0, abs(stairs[0][0] - people[k][0]) + abs(stairs[0][1] - people[k][1]))
    back(k+1, n)
    select[people[k]] = (1, abs(stairs[1][0] - people[k][0]) + abs(stairs[1][1] - people[k][1]))
    back(k+1, n)

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    board = []
    stairs = []
    people = []
    select = dict()
    for i in range(N):
        tmp = list(map(int, input().split()))
        board.append(tmp)
        for j in range(N):
            if tmp[j] > 1:
                stairs.append((i, j))
            elif tmp[j] == 1:
                people.append((i, j))
    result = 0xffff
    back(0, len(people))
    print('#{} {}'.format(tc, result))