def dfs(n, m, res):
    pass

dice = list(map(int, input().split()))
result = 0
boards = [
            [
                2, 4, 6, 8, 10,
                12, 14, 16, 18, 20,
                22, 24, 26, 28, 30,
                32, 34, 36, 38, 40
            ],
            [
                13, 16, 19, 25,
                1030, 35, 40
            ],
            [
                22, 24, 25, 1030, 35, 40
            ],
            [
                28, 27, 26, 25,
                1030, 35, 40
            ]
    ]
visit = [[0] * len(boards[i]) for i in range(len(boards))]
horse = {1: [0, -1], 2: [0, -1], 3: [0, -1], 4: [0, -1]}
dfs(0, 10, 0)
print(result)

