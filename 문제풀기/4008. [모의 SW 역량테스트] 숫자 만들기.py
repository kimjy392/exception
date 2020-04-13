def back(k, n, res):
    global MAX, MIN
    if k == n:
        MAX = max(MAX, res)
        MIN = min(MIN, res)
        return

    for i in range(4):
        if operations[i] > 0:
            operations[i] -= 1
            if i == 0:
                back(k+1, n, res+numbers[k+1])
            elif i == 1:
                back(k + 1, n, res - numbers[k + 1])
            elif i == 2:
                back(k + 1, n, res * numbers[k + 1])
            elif i == 3:
                tmp = res // numbers[k+1]
                if res % numbers[k+1] and res < 0:
                    tmp += 1
                back(k + 1, n, tmp)
            operations[i] += 1

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    operations = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    op = ['+', '-', '*', '//']
    MAX, MIN = -0xfffffff, 0xffffffff
    back(0, N-1, numbers[0])
    result = MAX - MIN
    print('#{} {}'.format(tc, result))
