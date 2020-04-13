A, B = map(int ,input().split())
N, M = map(int, input().split())
board = [[0] * A for _ in range(B)]
robots = []
# 1, 2, 3, 4
# 2, 3, 4, 1
# 4, 5, 6, 7


for i in range(1, N+1):
    tmp = list(input().split())
    board[B-int(tmp[1])][int(tmp[0])-1] = i
    if tmp[2] == 'E':
        tmp[2] = 1
    elif tmp[2] == 'S':
        tmp[2] = 2
    elif tmp[2] == 'W':
        tmp[2] = 3
    elif tmp[2] == 'N':
        tmp[2] = 4
    robots.append([B-int(tmp[1]), int(tmp[0])-1, tmp[2]])
dx = [0, 0, 1, 0, -1]
dy = [0, 1, 0, -1, 0]
flag = 0
for _ in range(M):
    order, command, r = input().split()
    x, y, d = robots[int(order)-1]
    if command == 'R':
        d = (d + int(r)) % 4
        if d == 0:
            d = 4
        robots[int(order) - 1] = [x, y, d]
    elif command == 'L':
        d = (d + int(r) * 3) % 4
        if d == 0:
            d = 4
        robots[int(order) - 1] = [x, y, d]
    else:
        for i in range(1, int(r)+1):
            tx, ty = x + dx[d] * i, y + dy[d] * i
            if -1 < tx < B and -1 < ty < A:
                if board[tx][ty]:
                    print('Robot {} crashes into robot {}'.format(order, board[tx][ty]))
                    flag = 1
                    break
                else:
                    board[tx][ty] = int(order)
                    board[tx-dx[d]][ty-dy[d]] = 0
                    robots[int(order) - 1] = [tx, ty, d]
            else:
                print('Robot {} crashes into the wall'.format(order))
                flag = 1
                break
    if flag:
        break



if not flag:
    print('OK')
