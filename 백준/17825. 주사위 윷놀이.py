def back(k, n):
    global ans
    if k == n:
        res = 0
        for mal in mals:
            res += mal[2]
        if ans < res:
            ans = res
        return
    for i in range(4):
        dx = dice[k]
        board, x, result = mals[i]
        tx = x + dx
        flag = 0
        if i in end:
            continue
        for j in range(4):
            if i == j:
                continue
            if (board, tx) in track[j]:
                flag = 1
                break
        if flag:
            continue
        tmp = track[i][:]
        if -1 < tx < len(boards[board]):
            score = boards[board][tx]
            if direction.get(score) and board == 0:
                mals[i] = [direction[score], -1, result + score]
                track[i] = [(direction[score], -1), (board, tx)]
            elif direction.get(score) and board > 0:
                mals[i] = [board, tx, result + score]
                track[i] = [(board, tx)]
            elif direction.get(score) == None:
                mals[i] = [board, tx, result + score]
                track[i] = [(board, tx)]
            back(k + 1, n)
            mals[i] = [board, x, result]
            track[i] = tmp[:]
        else:
            end.append(i)
            track[i] = []
            back(k+1, n)
            track[i] = tmp[:]
            end.pop()



dice = list(map(int, input().split()))
boards = [
            [
                2, 4, 6, 8, 10,
                12, 14, 16, 18, 20,
                22, 24, 26, 28, 30,
                32, 34, 36, 38, 40
            ],
            [
                13, 16, 19, 25,
                30, 35, 40
            ],
            [
                22, 24, 25, 30, 35, 40
            ],
            [
                28, 27, 26, 25,
                30, 35, 40
            ]
    ]
mals = [[0, -1, 0], [0, -1, 0], [0, -1, 0], [0, -1, 0]] # board, idx
direction = {10: 1, 20: 2, 30: 3}
ans = 0
track = [[], [], [], []]
end = []
back(0, len(dice))
print(ans)
