def back(k, n, res):
    global result
    if res == 0 or result >= res:
        return
    if k == n:
        if result < res:
            result = res
        return

    for i in range(N):
        if not visit[i]:
            visit[i] = True
            back(k+1, n, res*(board[k][i]*10**(-2)))
            visit[i] = False

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    visit = [False] * N
    result = 0
    back(0, N, 1)
    print('#{}'.format(tc), format(result*100, '0.6f'))