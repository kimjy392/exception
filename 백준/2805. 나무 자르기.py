# N, M = map(int, input().split())
#
# trees = list(map(int, input().split()))
# start = 0
# end = max(trees)
#
# while start <= end:
#     mid = (start + end) // 2
#     height = 0
#     for tree in trees:
#         if tree - mid > 0:
#             height += tree - mid
#         if height >= M:
#             break
#     if height >= M:
#         start = mid +1
#     else:
#         end = mid - 1
# print(end)
#
def solution(relation):
    answer_list = list()
    for i in range(1, 1 << len(relation[0])):
        tmp_set = set()
        for j in range(len(relation)):
            tmp = ''
            for k in range(len(relation[0])):
                if i & (1 << k):
                    tmp += str(relation[j][k])
            print(tmp)
            tmp_set.add(tmp)

        if len(tmp_set) == len(relation):
            not_duplicate = True
            for num in answer_list:
                if (num & i) == num:
                    not_duplicate = False
                    break
            if not_duplicate:
                answer_list.append(i)
    return len(answer_list)
solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]])
print(1<<len('abc'))
