from collections import deque

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    lock = deque(list(input()))
    numbers = set()
    div = len(lock) // 4
    for s in range(N):
        tmp = lock.popleft()
        lock.append(tmp)
        for sp in range(0, len(lock), div):
            num = '0x'
            for i in range(sp, sp+div):
                num += lock[i]
            numbers.add(int(num, 16))
    numbers = sorted(list(numbers), reverse=True)
    print('#{} {}'.format(tc, numbers[K-1]))