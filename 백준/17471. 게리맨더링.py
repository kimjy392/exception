def dfs(k, lst):
    global visit, cnt
    visit[k] = True
    cnt += 1
    for g in G[k]:
        if not visit[g] and g in lst:
            dfs(g, lst)

def back(k, n):
    global result, visit, cnt
    if k == n:
        B = list(set(range(1, N+1)) - set(A))
        if len(A) == 0 or len(A) == N:
            return
        cnt = 0
        for i in (A, B):
            visit = [False] * (N+1)
            dfs(i[0], i)
        if cnt == N:
            Atmp = 0
            Btmp = 0
            for i in A:
                Atmp += population[i]
            for i in B:
                Btmp += population[i]
            tmp = abs(Atmp - Btmp)
            if result > tmp:
                result = tmp
        return

    A.append(k)
    back(k+1, n)
    A.pop()
    back(k+1, n)

N = int(input())

population = [0] + list(map(int,input().split()))
G = [[] for _ in range(N+1)]
for j in range(1, N+1):
    tmp = list(map(int, input().split()))
    for i in range(1, len(tmp)):
        G[j].append(tmp[i])
result = 0xffffffff
A = []
back(1, N+1)
if result == 0xffffffff:
    print(-1)
else:
    print(result)