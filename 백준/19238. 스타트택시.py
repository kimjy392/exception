def find(start, energy):
    if guest.get(start):
        return (energy, start[0], start[1])
    visit = [[-1] * N for _ in range(N)]
    visit[start[0]][start[1]] = energy
    x, y = start
    stack = [(x, y, energy)]
    take = []
    while stack:
        x, y, energy = stack.pop(0)
        if energy <= 0:
            break
        for d in direction:
            dx, dy = d
            tx, ty = x + dx, y + dy
            if -1 < tx < N and -1 < ty < N and not board[tx][ty]:
                if visit[tx][ty] == -1:
                    visit[tx][ty] = energy - 1
                    stack.append((tx, ty, energy - 1))
    for key in guest:
        if visit[key[0]][key[1]] > 0:
            take.append((visit[key[0]][key[1]], key[0], key[1]))
    if take:
        take.sort(key= lambda x:(-x[0], x[1], x[2]))
        return take[0]
    return (-1, -1, -1)

def go(start, end, energy):
    visit = [[-1] * N for _ in range(N)]
    visit[start[0]][start[1]] = energy

    stack = [(start[0], start[1], energy)]

    while stack:
        x, y, tenergy = stack.pop(0)
        if tenergy < 0:
            break
        for d in direction:
            dx, dy = d
            tx, ty = x + dx, y + dy
            if -1 < tx < N and -1 < ty < N and not board[tx][ty] and visit[tx][ty] == -1:
                visit[tx][ty] = tenergy - 1
                stack.append((tx, ty, tenergy - 1))
    if visit[end[0]][end[1]] != -1:
        del guest[start]
        return (end[0], end[1], visit[end[0]][end[1]] + (energy - visit[end[0]][end[1]])*2)

    return (-1, -1, -1)
N, M, energy = map(int, input().split())

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
board = []
for _ in range(N):
    tmp = list(map(int, input().split()))
    board.append(tmp)
taxi = list(map(int, input().split()))
taxi = (taxi[0]-1, taxi[1]-1)
guest = dict()
for _ in range(M):
    sx, sy, ex, ey = list(map(int, input().split()))
    guest[(sx-1, sy-1)] = (ex-1, ey-1)

for i in range(M):
    result = find(taxi, energy)
    if result == (-1, -1, -1):
        energy = -1
        break
    taxi = (result[1], result[2])
    energy = result[0]
    result = go(taxi, guest[taxi], energy)
    if result == (-1, -1, -1):
        energy = -1
        break
    taxi = (result[0], result[1])
    energy = result[2]
print(energy)
