from collections import deque


def bfs(x):
    stack = deque([(x, 0)])

    while stack:
        x, time = stack.popleft()
        if x == K:
            return time
        for tx in [x-1, x+1, 2*x]:
            if -1 < tx < 100001 and (not load[tx] or load[tx] == 2):
                stack.append((tx, time+1))
                load[tx] = 1

N, K = map(int, input().split())
load = [0] * 100001
load[N], load[K] = 1, 2
print(bfs(N))