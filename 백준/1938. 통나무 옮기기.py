def check(tree):
    x = abs(tree[0][0] - tree[1][0])
    y = abs(tree[0][1] - tree[1][1])
    if x:
        return 2 # 세로
    if y:
        return 1 # 가로

N = int(input())
board = []
tree = []
des = []
for i in range(N):
    tmp = list(input())
    for j in range(len(tmp)):
        if tmp[j] == 'B':
            tree.append((i, j))
        elif tmp[j] == 'E':
            des.append((i, j))
    board.append(tmp)
direction = [[(-1, 0)], [(1, 0)], [(0, -1)], [(0, 1)], [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]]
visit = [[[] for _ in range(N)] for _ in range(N)]

stack = [(tree, check(tree) ,0)]
result = []
visit[tree[1][0]][tree[1][1]].append(check(tree))
while stack:
    tree, d,res = stack.pop(0)
    if sorted(tree) == sorted(des):
        result.append(res)
    for i in range(5):
        cnt = 0
        if i == 4:
            x = tree[1][0]
            y = tree[1][1]
            for dx, dy in direction[i]:
                tx, ty = x + dx, y + dy
                if -1 < tx < N and -1 < ty < N and board[tx][ty] != '1':
                    cnt += 1
            if cnt == 8:
                tmp = []
                if d == 1 and not 2 in visit[x][y]:
                    tmp = [(tree[1][0]-1, tree[1][1]), tree[1], (tree[1][0]+1, tree[1][1])]
                    visit[x][y].append(2)
                    stack.append((tmp, 2, res + 1))
                elif d == 2 and not 1 in visit[x][y]:
                    tmp = [(tree[1][0], tree[1][1]-1), tree[1], (tree[1][0], tree[1][1]+1)]
                    visit[x][y].append(1)
                    stack.append((tmp, 1, res + 1))
        else:
            dx, dy = direction[i][0]
            cx, cy = tree[1][0], tree[1][1]
            tmp = []
            for x, y in tree:
                tx, ty = x + dx, y + dy
                if -1 < tx < N and -1 < ty < N and board[tx][ty] != '1':
                    tmp.append((tx, ty))
                    cnt += 1
            if cnt == 3:
                nx, ny = cx + dx, cy + dy
                if not d in visit[nx][ny]:
                    visit[nx][ny].append(d)
                    stack.append((tmp, d, res + 1))

if result:
    result.sort()
    print(result[0])
else:
    print(0)
