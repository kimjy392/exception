def back(k, n):
    global result
    if k > n:
        return
    if k == n:
        tmp = 0
        for i in select:
            tmp += P[i]
        result = max(result, tmp)
        return


    select.append(k)
    back(k+T[k], n)
    select.pop()
    back(k+1, n)


N = int(input())
T = [0]
P = [0]
result = 0
for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)
select = []
back(1, N+1)
print(result)