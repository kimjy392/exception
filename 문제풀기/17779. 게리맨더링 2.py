N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
res = 0xffff
for x in range(N-2):
    for y in range(1, N-1): # 기준점
        # 경계선 만들기
        d1 = 0
        while 1:
            d1 += 1
            d2 = 1
            if not (x + d1 < N and y - d1 > -1 and x + d1 + d2 < N and -1 < y - d1 + d2 < N and x + d2 < N and y + d2 < N):
                break
            while x + d1 < N and y - d1 > -1 and x + d1 + d2 < N and -1 < y - d1 + d2 < N and x + d2 < N and y + d2 < N:
                flag = 0
                start = [0] * N
                end = [0] * N
                start[x] = y
                end[x] = y
                for i in range(1, d1+1):
                    tx = x + i
                    ty = y - i
                    if -1 < tx < N and -1 < ty < N:
                        start[tx] = ty
                    else:
                        flag = 1
                        break
                if flag:
                    break
                for i in range(1, d2+1):
                    tx = x + d1 + i
                    ty = y - d1 + i
                    if -1 < tx < N and -1 < ty < N:
                        start[tx] = ty
                    else:
                        flag = 1
                        break
                if flag:
                    break
                for i in range(1, d2+1):
                    tx = x + i
                    ty = y + i
                    if -1 < tx < N and -1 < ty < N:
                        end[tx] = ty
                    else:
                        flag = 1
                        break
                if flag:
                    break
                for i in range(1, d1+1):
                    tx = x + d2 + i
                    ty = y + d2 - i
                    if -1 < tx < N and -1 < ty < N:
                        end[tx] = ty
                    else:
                        flag = 1
                        break
                if flag:
                    break
                # 마지막에 d2 +=1
                result = [0] * 5
                for i in range(N):
                    for j in range(N):
                        if (start[i] or end[i]) and start[i] <= j <= end[i]:
                            result[4] += board[i][j]
                for i in range(x+d1):
                    if not start[i] and not end[i]:
                        for j in range(y+1):
                            result[0] += board[i][j]
                    else:
                        for j in range(start[i]):
                            result[0] += board[i][j]
                for i in range(x+d2+1):
                    if not start[i] and not end[i]:
                        for j in range(y+1, N):
                            result[1] += board[i][j]
                    else:
                        for j in range(end[i]+1, N):
                            result[1] += board[i][j]
                for i in range(x+d1, N):
                    if not start[i] and not end[i]:
                        for j in range(y-d1+d2):
                            result[2] += board[i][j]
                    else:
                        for j in range(start[i]):
                            result[2] += board[i][j]
                for i in range(x+d2+1, N):
                    if not start[i] and not end[i]:
                        for j in range(y-d1+d2, N):
                            result[3] += board[i][j]
                    else:
                        for j in range(end[i]+1, N):
                            result[3] += board[i][j]
                if res > max(result) - min(result):
                    # print(x, y, d1, d2)
                    # print(result)
                    res =  max(result) - min(result)
                d2 += 1
print(res)
