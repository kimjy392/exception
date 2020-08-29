# 다시풀기

t = int(input())

for testcase in range(t):
    N = int(input())
    home = list(map(int, input().split()))
    cons = dict()
    for _ in range(N):
        tmp = list(map(int, input().split()))
        cons[(tmp[0], tmp[1] )] = 1
    des = list(map(int, input().split()))
    stack = [[home[0], home[1], 20, 0]]
    visit = dict()
    visit[(home[0], home[1])] = 1

    while stack:
        x, y, beer, d = stack.pop(0)
        for direction in (1, 0), (-1, 0), (0, 1), (0, -1):
            dx, dy = direction
            tx, ty = x + dx, y + dy
            td = d + 1
            tbeer = beer
            if td // 50:
                tbeer -= 1
            if -32768 <= tx <= 32767 and -32768 <= ty <= 32767 and not visit.get((tx, ty)):
                visit[(tx, ty)] = 1
                stack.append((tx, ty, tbeer, td))

    print(visit.get((des[0], des[1])))