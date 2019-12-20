def back(k, n):
    global result
    if len(A) > N//2:
        return

    if k == n:
        if len(A) == N // 2:
            Ateam = 0
            Bteam = 0
            B = list(set(range(N)) - set(A))
            for i in range(len(A)):
                for j in range(i+1, len(A)):
                    Ateam += board[A[i]][A[j]]
                    Ateam += board[A[j]][A[i]]
            for i in range(len(B)):
                for j in range(i+1, len(B)):
                    Bteam += board[B[i]][B[j]]
                    Bteam += board[B[j]][B[i]]
            result = min(abs(Ateam - Bteam), result)
        return
    A.append(k)
    back(k+1, n)
    A.pop()
    back(k+1, n)

N = int(input())
result = 0xffffffff
board = [list(map(int ,input().split())) for _ in range(N)]
A = []
back(0, N)
print(result)