def back(k, n):
    global ans
    if k == n:
        res = 0
        for i in range(4):
            res += mals[i][2]
        if res > ans:
            ans = res
        return

    for i in range(4):
        dx = dice[k]
        board, x, result = mals[i]
        tx = x + dx
        flag = 0
        for j in range(4):
            if i == j:
                continue
            if [board, tx] in track[j]:
                flag = 1
                break
        if flag:
            continue
        tmp = track[i][:]
        if -1 < tx < len(boards[board]):
            score = boards[board][tx]
            if direction.get(score) and board == 0:
                mals[i] = [direction[score], 0, result+score]
                track[i] = [[direction[score], tx], [board, tx]]
            else:
                mals[i] = [board, tx, result+score]
                track[i] = [[board, tx]]
            back(k+1, n)
            mals[i] = [board, x, result]
            track[i] = tmp[:]
        else:
            track[i] = []
dice = list(map(int, input().split()))
boards = [
            [   0,
                2, 4, 6, 8, 10,
                12, 14, 16, 18, 20,
                22, 24, 26, 28, 30,
                32, 34, 36, 38, 40
            ],
            [
                10, 13, 16, 19, 25,
                30, 35, 40
            ],
            [
                20, 22, 24, 25, 30, 35, 40
            ],
            [
                30, 28, 27, 26, 25,
                30, 35, 40
            ]
    ]
mals = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]] # board, idx, result
track = [[0, 0] for _ in range(4)]
direction = {10: 1, 20: 2, 30: 3}
ans = 0
back(0, len(dice))
print(ans)
