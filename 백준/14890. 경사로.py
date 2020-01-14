def check(x, y, k):
    visit = [False] * N
    if k:
        for i in range(1, N):
            if abs(board[i][y] - board[i-1][y]) == 1:
                lst = []
                if board[i][y] > board[i-1][y]:
                    for j in range(1, L+1):
                        if -1 < i-j < N and board[i-1][y] == board[i-j][y] and not visit[i-j]:
                            lst.append(i-j)
                        else:
                            return 0
                    if len(lst) == L:
                        for dx in lst:
                            visit[dx] = True
                    else:
                        return 0
                else:
                    for j in range(L):
                        if -1 < i+j < N and board[i][y] == board[i+j][y] and not visit[i+j]:
                            lst.append(i+j)
                        else:
                            return 0
                    if len(lst) == L:
                        for dx in lst:
                            visit[dx] = True
                    else:
                        return 0

            elif board[i][y] - board[i-1][y] == 0:
                continue
            else:
                return 0


    else:
        for i in range(1, N):
            if abs(board[x][i] - board[x][i-1]) == 1:
                lst = []
                if board[x][i] > board[x][i-1]:
                    for j in range(1, L + 1):
                        if -1 < i - j < N and board[x][i-1] == board[x][i-j] and not visit[i - j]:
                            lst.append(i - j)
                        else:
                            return 0
                    if len(lst) == L:
                        for dx in lst:
                            visit[dx] = True
                    else:
                        return 0
                else:
                    for j in range(L):
                        if -1 < i + j < N and board[x][i] == board[x][i + j] and not visit[i + j]:
                            lst.append(i + j)
                        else:
                            return 0
                    if len(lst) == L:
                        for dx in lst:
                            visit[dx] = True
                    else:
                        return 0

            elif board[x][i] - board[x][i-1] == 0:
                continue
            else:
                return 0


    return 1

N, L = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for i in range(N):
    ans += check(i, 0, 0) # 가로
    ans += check(0, i, 1) # 세로
    # if check(i, 0, 0):
    #     print(i, 0, '가로')
    #     ans += 1
    # if check(0, i, 1):
    #     print(0, i, '세로')
    #     ans += 1

print(ans)
