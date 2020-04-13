def back(k, n, s):
    global result
    if k >= n:
        result = min(result, s)
        return
    elif y < s:
        return
    if swim[k]:
        back(k+1, n, s+swim[k]*d)
        back(k+1, n, s+m)
        back(k+3, n, s+m3)
    else:
        back(k+1, n, s)

T = int(input())
for tc in range(1, T+1):
    d, m, m3, y = map(int, input().split())
    swim = list(map(int, input().split()))
    result = y
    back(0, 12, 0)
    print('#{} {}'.format(tc, result))