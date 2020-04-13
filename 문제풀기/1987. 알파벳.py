def search(x, y, res):
    global result
    if result < res:
        result = res

    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        tx = x + dx; ty = y + dy
        if 0 > tx or N-1 < tx or ty < 0 or ty > M-1:
            continue
        a = ord(alpa[tx][ty]) - ord('A')
        if not myalpa[a]:
            myalpa[a] += 1
            search(tx, ty, res+1)
            myalpa[a] -= 1
N, M = map(int, input().split())
myalpa = [0] * 26
alpa = [list(input()) for _ in range(N)]
result = 0
myalpa[ord(alpa[0][0])-ord('A')] = 1
search(0, 0, 1)
print(result)
