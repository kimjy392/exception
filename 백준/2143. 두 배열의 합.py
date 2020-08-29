T = int(input())

n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

Al, Ar, As = 0, 0, 0
Bl ,Br, Bs = 0, 0, 0
result = 0

while 1:
    if Ar >= len(A):
        break
    Ar += 1
    As = sum(A[Al:Ar])
    while Al < Ar:
        while As <= T:
            if As + Bs > T and Bl < Br-1:
                Bl += 1
                Bs -= B[Bl -1]
            elif Br >= len(B):
                Bl, Br, Bs = 0, 0, 0
                break
            else:
                Br += 1
                Bs += B[Br - 1]
            if As + Bs == T:
                result += 1
        Al += 1
        As -= A[Al-1]
    Al = 0


print(result)