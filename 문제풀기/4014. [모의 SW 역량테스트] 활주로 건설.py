T = int(input())

for tc in range(1, T+1):
    N, x = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    visit = [[False] * N for _ in range(N)]
    for i in range(N):
        tmp = 0
        cnt = 0
        for j in range(N-1):
            if abs(board[i][j] - board[i][j+1]) == 1:
                flag = 0
                if board[i][j] > board[i][j + 1]:
                    for tj in range(1, x+1):
                        if 0 > j+tj or j+tj > N-1 or visit[i][j+tj] or board[i][j+1] != board[i][j+tj]:
                            flag = 1
                            break
                    if flag:
                        tmp = 0
                        break
                    for tj in range(1, x+1):
                        visit[i][j+tj] = True

                else:
                    for tj in range(x):
                        if 0 > j-tj or j-tj > N-1 or board[i][j] != board[i][j-tj] or visit[i][j-tj]:
                            flag = 1
                            break
                    if flag:
                        tmp = 0
                        break
                    for tj in range(x):
                        visit[i][j-tj] = True
                tmp += 1
            elif abs(board[i][j] - board[i][j+1]) > 1:
                tmp = 0
                break
            elif abs(board[i][j] - board[i][j+1]) == 0:
                cnt += 1
        if tmp:
            result += 1
        elif cnt == N-1:
            result += 1
    visit = [[False] * N for _ in range(N)]
    for j in range(N):
        tmp = 0
        cnt = 0
        for i in range(N - 1):
            if abs(board[i][j] - board[i+1][j]) == 1:
                flag = 0
                if board[i][j] > board[i+1][j]:
                    for ti in range(1, x + 1):
                        if 0 > i + ti or i + ti > N - 1 or board[i+1][j] != board[i+ti][j] or visit[i+ti][j]:
                            flag = 1
                            break
                    if flag:
                        tmp = 0
                        break
                    for ti in range(1, x + 1):
                        visit[i+ti][j] = True

                else:
                    for ti in range(x):
                        if 0 > i-ti or i-ti > N - 1 or board[i][j] != board[i-ti][j] or visit[i-ti][j]:
                            flag = 1
                            break
                    if flag:
                        tmp = 0
                        break
                    for ti in range(x):
                        visit[i-ti][j] = True
                tmp += 1
            elif abs(board[i][j] - board[i+1][j]) > 1:
                tmp = 0
                break
            elif abs(board[i][j] - board[i+1][j]) == 0:
                cnt += 1
        if tmp:
            result += 1
        elif cnt == N -1:
            result += 1
    print('#{} {}'.format(tc, result))