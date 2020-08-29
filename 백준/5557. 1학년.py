N = int(input())
numbers = list(map(int, input().split()))
board = [[0] * 21 for _ in range(N-1)]
board[0][numbers[0]] = 1
for i in range(1, N-1):
    for k in range(21):
        if 0 <= k + numbers[i] < 21:
            board[i][k+numbers[i]] += board[i-1][k]
        if 0 <= k - numbers[i] < 21:
            board[i][k-numbers[i]] += board[i-1][k]
print(board[-1][numbers[-1]])
