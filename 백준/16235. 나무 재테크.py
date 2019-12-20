from collections import deque

def spring():
    a = 0
    for i in range(N):
        for j in range(N):
            if len(trees[i][j]) > 0:
                a = 1
                tmp = nut[i][j]
                cnt = -1
                for k in range(len(trees[i][j])):
                    tmp -= trees[i][j][k]
                    if tmp < 0:
                        cnt = k
                        break
                    else:
                        trees[i][j][k] += 1
                if tmp < 0:
                    nut[i][j] = 0
                else:
                    nut[i][j] = tmp
                if cnt != -1:
                    for _ in range(len(trees[i][j]) - cnt):
                        s2d2[i][j] += (trees[i][j].pop() // 2)
    return a

def fall():
    for i in range(N):
        for j in range(N):
            nut[i][j] += s2d2[i][j]
            if len(trees[i][j]) > 0:
                for k in range(len(trees[i][j])):
                    if not trees[i][j][k] % 5:
                        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
                            tx = i + dx
                            ty = j + dy
                            if -1 < tx < N and -1 < ty < N:
                                trees[tx][ty].appendleft(1)



N, M, K = map(int, input().split())
nut = [[5] * N for _ in range(N)]
trees = [[deque() for _ in range(N)] for _ in range(N)]
s2d2 = [list(map(int, input().split())) for _ in range(N)]
for _ in range(M):
    x, y, age = map(int, input().split())
    trees[x-1][y-1].append(age)
year = 0
b = 0
while year < K:
    b = spring()
    if not b:
        break
    fall()
    year += 1
result = 0
if b:
    for i in range(N):
        for j in range(N):
            result += len(trees[i][j])
    print(result)
else:
    print(0)
