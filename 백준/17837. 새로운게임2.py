from collections import deque
N, K = map(int, input().split())
# 0 : 흰색, 1 : 빨간색, 2: 파란색
# 1 : 오른쪽, 2: 왼쪽, 3: 위, 4: 아래
board = [list(map(int, input().split())) for _ in range(N)]
mal = dict()
upmal = [ [deque([]) for _ in range(N)]  for _ in range(N)]
for i in range(K):
    x, y, d = map(int, input().split())
    mal[i] = [x-1, y-1, d]
    upmal[x-1][y-1].append(i)
move = [[], (0, 1), (0, -1), (-1, 0), (1, 0)]
direction = {1: 2, 2: 1, 3: 4, 4: 3}
result = -1
for cnt in range(1, 1001):
    for i in range(K):
        selectmal = mal[i]
        tmp = deque()
        for idx in range(len(upmal[selectmal[0]][selectmal[1]])):
            upmalidx = upmal[selectmal[0]][selectmal[1]].popleft()
            tmp.append(upmalidx)
            if upmalidx == i:
                break
        x, y, d = mal[i][0], mal[i][1], mal[i][2]
        tx = x + move[d][0]
        ty = y + move[d][1]
        if -1 < tx < N and -1 < ty < N and -1 < board[tx][ty] < 2:
            for malidx in tmp:
                mal[malidx][0] = tx
                mal[malidx][1] = ty
            if board[tx][ty] == 0:
                tmp.reverse()
            upmal[tx][ty].extendleft(tmp)
        elif (-1 < tx < N and -1 < ty < N and board[tx][ty] == 2) or tx < 0 or tx > N -1 or ty < 0 or ty > N-1: # 끝에 가면
            d = direction[d] # 방향을 바꾸고
            # 뒤에가 파란색인지 끝인지 확인하고
            dx, dy = move[d]
            nx = x + dx
            ny = y + dy
            mal[i][2] = d
            if -1 < nx < N and -1 < ny < N and board[nx][ny] == 2:
                tmp.reverse()
                upmal[x][y].extendleft(tmp)
            elif -1 < nx < N and -1 < ny < N and -1 < board[nx][ny] < 2:
                for malidx in tmp:
                    mal[malidx][0] = nx
                    mal[malidx][1] = ny
                if board[nx][ny] == 0:
                    tmp.reverse()
                upmal[nx][ny].extendleft(tmp)
            else:
                tmp.reverse()
                upmal[x][y].extendleft(tmp)
        if len(upmal[mal[i][0]][mal[i][1]]) >= 4:
            result = cnt
            break
    if result > -1:
        break


print(result)