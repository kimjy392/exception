# def back(k, n, res):
#     if k == n:
#         result.add(res)
#         return
#     if memo[k][res]:
#         return
#     else:
#         memo[k][res] = 1
#         back(k+1, n, res+scores[k])
#         back(k+1, n, res)
#
# T = int(input())
#
# for tc in range(1, T+1):
#     N = int(input())
#     scores = list(map(int, input().split()))
#     memo = [[0] *N*max(scores) for _ in range(N)]
#     result = set()
#     back(0, N, 0)
#     print('#{} {}'.format(tc, len(result)))

# T = int(input())
#
# for tc in range(1, T+1):
#     N = int(input())
#     scores = list(map(int, input().split()))
#     result = set([0])
#
#     for score in scores:
#         tmp = set()
#         for res in result:
#             tmp.add(score+res)
#         result = tmp | result
#     print('#{}'.format(tc),len(result))

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    scores = list(map(int, input().split()))
    result = [0]
    MAX = ((N*max(scores))+1)
    memo = [0] * MAX
    for score in scores:
        tmp = []
        for res in result:
            if score + res < MAX and not memo[score+res]:
                tmp.append(score+res)
                memo[score+res] = 1
        result+=tmp
    print('#{}'.format(tc), len(result))