# def count():
#     global isuse
#     isuse = [False] * W
#     for j in range(W):
#         i, start, cnt = 0, 0, 0
#         while i < D:
#             if tboard[start][j] == tboard[i][j]:
#                cnt += 1
#             else:
#                 cnt = 0
#                 start = i
#                 continue
#             if cnt == K:
#                 isuse[j] = True
#                 break
#             i += 1
#     if sum(isuse) == W:
#         return True
#     else:
#         return False
# def Cback(k, n):
#     global tboard, result, isuse, abc
#     if k == n:
#         if result <= D - len(Cselect):
#             return
#         for i in Cselect:
#             tboard[i] = board[i]
#         if count():
#             if (D - len(Cselect)) < result:
#                 result = (D - len(Cselect))
#                 tmp = [-1] * D
#                 for i in range(D):
#                     if i not in Cselect:
#                         tmp[i] = Mselect[i]
#                 abc.append(tmp)
#
#         for i in Cselect:
#             tboard[i] = [Mselect[i]] * W
#         return
#
#     Cselect.append(k)
#     Cback(k+1, n)
#     Cselect.pop()
#     Cback(k+1, n)
#
# def Mback(k, n):
#     global tboard, abc
#     if k == n:
#         for j in range(len(abc)):
#             for i in range(D):
#                 if abc[j][i] == Mselect[i]:
#                     return
#         tboard = []
#         for i in Mselect:
#             tboard.append([i] * W)
#         Cback(0, D)
#         return
#
#
#     Mselect.append(1)
#     Mback(k+1, n)
#     Mselect.pop()
#     Mselect.append(0)
#     Mback(k+1, n)
#     Mselect.pop()
#
# T = int(input())
#
# for tc in range(1, T+1):
#     D, W, K = map(int, input().split())
#     board = [list(map(int, input().split())) for _ in range(D)]
#     Mselect = []
#     result = 0xfff
#     Cselect = []
#     abc = []
#     Mback(0, D)
#     print('#{} {}'.format(tc, result))
from collections import deque
def count():
    global tboard
    isuse = [False] * W
    for j in range(W):
        i, start, cnt = 0, 0, 0
        while i < D:
            if tboard[start][j] == tboard[i][j]:
               cnt += 1
            else:
                cnt = 0
                start = i
                continue
            if cnt == K:
                isuse[j] = True
                break
            i += 1
    if sum(isuse) == W:
        return True
    else:
        return False

# def bfs():
#     global result, tboard
#     stack = deque([(0, D, 0, [])])
#
#     while stack:
#         k, n, res, tmp = stack.popleft()
#
#         tboard = []
#         for i in range(len(tmp)):
#             if tmp[i] == -1:
#                 tboard.append(board[i])
#             else:
#                 tboard.append([tmp[i]] * W)
#         if count():
#             if res < result:
#                 result = res
#         for i in -1, 0, 1:
#             if i == -1:
#                 stack.append((k+1, n, res, tmp[:]+[-1]))
#             else:
#                 stack.append((k+1, n, res+1, tmp[:]+[i]))

def back(k, n, res):
    global result
    if res >= result:
        return
    if count():
        if res < result:
            result = res
    if k == n:
        return
    if -1 not in visit[k]:
        visit[k].append(-1)
        back(k+1, n, res)
    for i in range(2):
        if i not in visit[k]:
            tmp, board[k] = board[k], [i] * W
            visit[k].append(i)
            back(k+1, n, res+1)
            board[k] = tmp


T = int(input())
for tc in range(1, T+1):
    D, W, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(D)]
    visit = [[] for _ in range(D)]
    result = 0xfff
    # back(0, D, 0)
    bfs()
    print('#{} {}'.format(tc, result))
