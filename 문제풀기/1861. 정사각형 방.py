import sys
from collections import deque
sys.stdin = open('n1000.txt', 'r')

def bfs(x, y):
    stack = deque([(x, y)])
    while stack:
        x, y = stack.popleft()

        for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
            tx, ty = x + dx, y + dy
            if -1 < tx < N and -1 < ty < N and board[tx][ty] - board[x][y] == 1 and not visit[board[tx][ty]]:
                visit[board[tx][ty]] = 1
                stack.append((tx, ty))

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int ,input().split())) for _ in range(N)]
    visit = [0] * (N*N+1)
    res, result = 0, 0
    for i in range(N):
        for j in range(N):
            bfs(i, j)
    cnt = 0
    for i in range(N*N, -1, -1):
        if visit[i] == 1:
            cnt += 1
        else:
            if result <= cnt:
                result = cnt
                res = i+1
            cnt = 0
    print('#{} {} {}'.format(tc, res-1, result+1))

# tc = int(input())
# for t in range(1, tc + 1):
#     N = int(input())
#     nums = [list(map(int, input().split())) for _ in range(N)]
#     arr = [0] * (N * N + 1)
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]
#     max_cnt = -1
#
#     for i in range(N):
#         for j in range(N):
#             for k in range(4):
#                 if 0 <= i + dx[k] < N and 0 <= j + dy[k] < N:
#                     if nums[i + dx[k]][j + dy[k]] - 1 == nums[i][j]:
#                         arr[nums[i][j]] = 1
#                         break
#
#     for i in range(1, N * N):
#         if arr[i] == 1 and arr[i - 1] == 0:
#             cnt = 1
#             while True:
#                 if arr[i + cnt] == 1:
#                     cnt += 1
#                 else:
#                     break
#
#             if max_cnt < (cnt + 1):
#                 max_cnt = cnt + 1
#                 result_num = i
#
#     print(f'#{t} {result_num} {max_cnt}')

# T = int(input())
# for tc in range(1, T + 1):
#     n = int(input())
#     nums = [list(map(int, input().split())) for _ in range(n)]
#     v = [0] + [0] * n ** 2
#
#     dx = [0, 1, 0, -1]
#     dy = [1, 0, -1, 0]
#     for i in range(n):
#         for j in range(n):
#             for k in range(4):
#                 ni = i + dx[k]
#                 nj = j + dy[k]
#                 if 0 <= ni < n and 0 <= nj < n:
#                     if nums[ni][nj] == (nums[i][j] + 1):
#                         v[nums[i][j]] = 1
#
#     t_num, t_cnt, length = 0, 0, 0
#     for i in range(1, n ** 2 + 1):
#         if v[i]:
#             length += 1
#         elif not v[i] and length:
#             if t_cnt < length:
#                 t_cnt = length
#                 t_num = i - length
#             length = 0
#
#     print('#{} {} {}'.format(tc, t_num, t_cnt + 1))