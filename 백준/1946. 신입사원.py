import sys

T = int(input())
for _ in range(T):
    N = int(input())
    candidate = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    candidate.sort()
    tmp = 0
    minc = 0
    for i in range(N):
        x, y = candidate[i]
        _, y1 = candidate[minc]
        if y > y1:
            tmp += 1
        if y < y1:
            minc = i
    result = N - tmp
    print(result)
