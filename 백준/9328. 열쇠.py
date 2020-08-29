from collections import deque

def move(command):
    if command == 1: # 동쪽
        hor.append(hor.popleft())
        ver[1], ver[3] = hor[1], hor[3]

    elif command == 2: # 서쪽
        hor.appendleft(hor.pop())
        ver[1], ver[3] = hor[1], hor[3]
    elif command == 3: # 북쪽
        # 6, 2, 1, 5
        ver.appendleft(ver.pop())
        hor[1], hor[3] = ver[1], ver[3]
    else: # 남쪽
        ver.append(ver.popleft())
        hor[1], hor[3] = ver[1], ver[3]


N, M ,fx, fy ,K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
commands = list(map(int, input().split()))
value = { x:0 for x in range(1, 7)}
dice = {1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}
d = [(), (0, 1), (0, -1), (-1, 0), (1, 0)]
hor = deque([4, 1, 3, 6])
ver = deque([2, 1, 5, 6])
for command in commands:
    tx, ty = fx +d[command][0], fy + d[command][1]
    if -1 < tx < N and -1 < ty < M:
        move(command)
        if board[tx][ty] == 0:
            board[tx][ty] = value[ver[1]]
        else:
            value[ver[1]] = board[tx][ty]
            board[tx][ty] = 0
        print(value[ver[3]])
        fx, fy = tx, ty